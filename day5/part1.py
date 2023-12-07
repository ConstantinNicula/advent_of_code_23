import sys

def skip_line():
    _ = sys.stdin.readline()

def str_to_list(input: str) -> list[int]:
    input = input.strip(' ')
    return [int(v) for v in input.split(' ') if len(v)]

def read_map():
    ret = []
    for line in sys.stdin: 
        line_s = line.rstrip()
        if not line_s:
            break
        ret.append(str_to_list(line_s))
    return ret 

def read_input():
    seeds = str_to_list(sys.stdin.readline().rstrip().split(':')[1])
    skip_line()
    maps, num_maps = [], 7
    for i in range(num_maps):
        skip_line()
        maps.append(read_map()) 
    return (seeds, maps) 

def transform_once(val: int, map: list[list[int]]) -> int:
    for dest, st, length in map: 
        if val >= st and val <= st + length-1:
            return dest + val - st
    return val

def transform_multiple(val: int, maps: list) -> int:
    for m in maps: 
        val = transform_once(val, m)
    return val

def solve(seeds: list[int], maps: list):
    dest_locs = map(lambda s: transform_multiple(s, maps), seeds)
    print(min(dest_locs)) 

def main():
    seeds, maps = read_input()
    print(seeds)
    solve(seeds, maps)

if __name__ == "__main__":
    main()
