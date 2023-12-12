import sys 

def read_input()-> list[str, list[int]]:
    out = []
    for line in sys.stdin:
        line = line.rstrip()
        record, arr = line.split(' ')
        arr = [int(x) for x in arr.split(',')]
        out.append((record, arr))
    return out 

def bt_match(record: str, i: int, arr: list[int], j:int, res=[]) -> int:
    if j == len(arr):
        # sanity check 
        for k in range(min(len(record), len(res))):
            if res[k] == '#' and record[k] == '.':
                print(f"{''.join(res)}") 
                sys.exit()
            if res[k] == '.' and record[k] == '#':
                print(f"{''.join(res)}") 
                sys.exit()
        return 1 if record[i:].count('#') == 0 else 0 
    cnt = 0
    for o in range(i, len(record)):
        # if can match
        if o + arr[j] > len(record):
            break 
        
        if record[o: o + arr[j]].count('.') == 0:
            if (o + arr[j] < len(record) and record[o + arr[j]] != '#') or (o + arr[j] >= len(record)):
                cnt += bt_match(record, o + arr[j] + 1, arr, j+1, res = res + ['.']*(o-i) + ['#']* arr[j] + ['.']) 

        # can't skip over it
        if record[o] == '#': break
    return cnt 

def solve(input: list[str, list[int]]):

    sum = 0
    for record, arr in input:
        cnt = bt_match(record, 0, arr, 0)
        sum += cnt
    print(sum)
    pass 


def main():
    input = read_input()
    solve(input)

if __name__ == "__main__":
    main()