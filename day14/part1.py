import sys

def read_input():
    out = []
    for line in sys.stdin:
        out.append(line.rstrip())
    return out

def solve(grid: list[str]):
    grid_t = [''.join(line) for line in zip(*grid) ]
    comp_grid_t = []
    for line in grid_t:
        comp_line = ['.'] * len(line)
        i = 0
        for j, c in enumerate(line):
            if c == 'O':
                comp_line[i] = 'O'
                i += 1
            elif c == '#':
                comp_line[j] = '#'
                i = j+1 

        comp_grid_t.append(''.join(comp_line))

    comp_grid = [''.join(line) for line in zip(*comp_grid_t)]
    res = 0
    for i, line in enumerate(comp_grid):
        res += (len(comp_grid[0]) - i) * line.count('O')
    print(res)

def main():
    input = read_input()
    print(input)
    solve(input)

if __name__ == "__main__":
    main()