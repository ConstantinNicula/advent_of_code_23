import sys

def read_input():
    ret = []

    chunk = []
    for line in sys.stdin:
        if line != "\n":
            chunk.append(line.strip())
        else:
            ret.append(chunk)
            chunk = [] 
    ret.append(chunk)
    return ret

def count_diff(a:list[str], b: list[str]):
    err = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                err+=1 
    return err

def find_symmetry(pat: list[str]) -> int:
    for i in range(1, len(pat)):
        span = min(i, len(pat)-i)
        left = pat[max(0, i-span): i]
        right = pat[i: min(len(pat), i+span)]
        right.reverse()
        if count_diff(left, right) == 1:
            return i

    return -1

def solve(patterns: list[list[str]]):
    sum = 0
    for pat in patterns:
        row_i = find_symmetry(pat) 
        if  row_i != -1:
            sum += row_i * 100
            continue
        
        # transpose pattern
        pat_t = [''.join(line) for line in zip(*pat)]
        col_i = find_symmetry(pat_t)
        if col_i != -1:
            sum += col_i
            continue
        
        assert row_i !=-1 or col_i != -1
    print(sum)

def main():
    input = read_input()
    print(input)
    solve(input)

if __name__ == "__main__":
    main()