import sys
import re

def read_input() -> list[str]:
    ret = []
    for line in sys.stdin:
        ret.append(line.rstrip())
    return ret

def exists_val_in_interval(interval: tuple[int, int], values: list[int]) -> bool:
    min_v, max_v = interval
    for val in values:
        if val >= min_v and val <= max_v:
            return True 
    return False

def solve(schematic: list[str]) -> int:
    schematic_nums = [] # [ [(st, end), ], ..]
    schematic_syms = [] # [ [idx1, idx2], ..]

    # extract data
    for line in schematic:
        schematic_nums.append([m.span() for m in re.finditer(r"[0-9]+", line)])
        schematic_syms.append([m.start(0) for m in re.finditer(r"[^0-9\.]", line)])
    
    # check valid number 
    sum = 0
    for row_idx, row_nums in enumerate(schematic_nums): 
        for num in row_nums:
            st, end = num
            
            # check in row 
            if exists_val_in_interval((st-1, end), schematic_syms[row_idx]):
                sum += int(schematic[row_idx][st: end])

            # linear search check above row
            if row_idx - 1 >= 0:
                if exists_val_in_interval((st-1, end), schematic_syms[row_idx-1]):
                    sum += int(schematic[row_idx][st: end]) 

            # linear search check below row 
            if row_idx + 1 < len(schematic_nums):
                if exists_val_in_interval((st-1, end), schematic_syms[row_idx+1]):
                    sum += int(schematic[row_idx][st: end])
    print(sum)

def main():
    input = read_input()
    solve(input) 

if __name__ == "__main__":
    main()