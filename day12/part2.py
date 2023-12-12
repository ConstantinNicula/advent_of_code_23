import sys 

def read_input()-> list[str, list[int]]:
    out = []
    for line in sys.stdin:
        line = line.rstrip()
        record, arr = line.split(' ')
        arr = [int(x) for x in arr.split(',')]
        out.append((record, arr))
    return out 

def bt_match(record: str, i: int, arr: list[int], j:int, memo={}) -> int:
    if (i, j) in memo:
        return memo[(i, j)] 
    if j == len(arr):
        res = 1 if record[i:].count('#') == 0 else 0 
        memo[(i, j)] = res
        return res
    cnt = 0
    for o in range(i, len(record)):
        # if can match
        if o + arr[j] > len(record):
            break 
        
        if record[o: o + arr[j]].count('.') == 0:
            if (o + arr[j] < len(record) and record[o + arr[j]] != '#') or (o + arr[j] >= len(record)):
                cnt_sub_arr = bt_match(record, o + arr[j] + 1, arr, j+1, memo=memo) 
                memo[(o+arr[j]+1, j+1)] = cnt_sub_arr 
                cnt += cnt_sub_arr
        # can't skip over it
        if record[o] == '#': break
    return cnt 

def solve(input: list[str, list[int]]):
    # dup
    dup_input = []
    for record, arr in input: 
        dup_rec = '?'.join([record]*5)
        dup_arr = arr * 5 
        dup_input.append((dup_rec, dup_arr))

    sum = 0
    for record, arr in dup_input:
        print(f'{record}')
        cnt = bt_match(record, 0, arr, 0, {})
        sum += cnt
    print(sum)
    pass 


def main():
    input = read_input()
    solve(input)

if __name__ == "__main__":
    main()