import sys
import re

def read_input() -> list[str]:
    ret = []
    for line in sys.stdin:
        ret.append(line.rstrip())
    return ret

def get_adjacent_num(value: int, intervals: list[tuple[int]], schematic: str) -> list[tuple[int]]:
    ret = [] 
    for min_v, max_v in intervals:
        if value >= min_v-1 and value <= max_v:
            ret.append((min_v, max_v, int(schematic[min_v: max_v])))

        if len(ret) == 2:
            break
    return ret

def solve(schematic: list[str]) -> int:
    schematic_nums = [] # [ [(st, end), ], ..]
    schematic_syms = [] # [ [idx1, idx2], ..]

    # extract data
    for line in schematic:
        schematic_nums.append([m.span() for m in re.finditer(r"[0-9]+", line)])
        schematic_syms.append([m.start(0) for m in re.finditer(r"\*", line)])
    
    # check valid number 
    sum = 0
    for row_idx, row_syms in enumerate(schematic_syms): 
        for sym_idx in row_syms:
            adj_list = []

            # find adjacent in row 
            query_res = get_adjacent_num(sym_idx, schematic_nums[row_idx], schematic[row_idx])
            if query_res: adj_list.extend(query_res)                 

            # find adjacent above 
            if row_idx - 1 >= 0:
                query_res = get_adjacent_num(sym_idx, schematic_nums[row_idx-1], schematic[row_idx -1])
                if query_res: adj_list.extend(query_res)

            # find adjacent below
            if row_idx + 1 < len(schematic_nums):
                query_res = get_adjacent_num(sym_idx, schematic_nums[row_idx+1], schematic[row_idx + 1])
                if query_res: adj_list.extend(query_res)

            if len(adj_list) == 2: 
                num1, num2 = adj_list[0][2], adj_list[1][2]
                sum += num1 * num2 
    print(sum)

def main():
    input = read_input()
    solve(input) 

if __name__ == "__main__":
    main()