import sys

def read_input() -> list[list[chr]]:
    ret = []
    for line in sys.stdin:
        ret.append([*line.rstrip()])
    return ret

def expand(m: list[list[chr]]):
    for _ in range(2):
        out_m = []
        for line in m: 
            if line.count('.') == len(line):
                out_m.append(line)
            out_m.append(line)
        m = list(zip(*out_m))

    return m

def solve(m: list[list[chr]]):
    # expand map
    exp_m = expand(m)

    # find stars 
    stars = []
    for i, row in enumerate(exp_m):
        for j, tile in enumerate(row):
            if tile == '#':
                stars.append((i, j)) 

    # compute min distances 
    sum = 0
    for i in range(len(stars) - 1):
        for j in range(i + 1 , len(stars)):
            dist = abs(stars[i][0] - stars[j][0]) + abs(stars[i][1] - stars[j][1])
            sum += dist
    
    print(sum)

def main(): 
    input = read_input()
    solve(input)

if __name__ == "__main__":
    main()