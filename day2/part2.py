import sys


def read_cubes(input: str) -> tuple[int]:
    type_to_idx = {"red": 0, "green": 1, "blue": 2}
    ret = [0] * 3
    cube_sets = input.split(',')  
    for cube in cube_sets:
        count, type = cube.lstrip().split(' ')
        ret[type_to_idx[type]] = int(count)    
    return tuple(ret)

def read_input() -> list:
    ret = []
    for line in sys.stdin:
        line = line.rstrip()

        # get game id
        game_name, game_info  = line.split(":")        
        
        # parse info
        game_idx = int(game_name.split(' ')[1])  
        extracted_cubes = [read_cubes(cubes) for cubes in game_info.split(';')]
        ret.append((game_idx, extracted_cubes))

    return ret

def solve(games: list): 
    sum = 0
    for game in games:
        idx, draws = game 
        min_r, min_g, min_b = (1, 1, 1)
        for draw in draws:
            min_r = max(min_r, draw[0])
            min_g = max(min_g, draw[1])
            min_b = max(min_b, draw[2])
        power = min_r * min_b * min_g
        sum += power
    print(sum)

def main():
    data = read_input()
    solve(data)
    pass


if __name__ == "__main__":
    main()