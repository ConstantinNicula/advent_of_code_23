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

def find_symmetry(pat: list[str]) -> int:
    for i in range(1, len(pat)):
        span = min(i, len(pat)-i)
        left = pat[max(0, i-span): i]
        right = pat[i: min(len(pat), i+span)]
        right.reverse()
        if left == right:
            return i

    return -1

def solve(patterns: list[list[str]]):
    sum = 0
    for pat in patterns:
        row_i = find_symmetry(pat) 
        if  row_i != -1:
            sum += row_i * 100
            print(row_i)
            continue
        
        # transpose pattern
        pat_t = [''.join(line) for line in zip(*pat)]
        col_i = find_symmetry(pat_t)
        if col_i != -1:
            sum += col_i
            print(col_i)
            continue
        
        assert row_i !=-1 or col_i != -1
    print(sum)

def main():
    input = read_input()
    print(input)
    solve(input)

if __name__ == "__main__":
    main()