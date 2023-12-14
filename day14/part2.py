import sys

def read_input():
    out = []
    for line in sys.stdin:
        out.append(list(line.rstrip()))
    return out

def shift_up(grid: list[list[chr]]):
    for j in range(len(grid[0])):
        k = 0 
        for i in range(len(grid)):
            c = grid[i][j]
            if c == 'O':
                tmp = grid[k][j]
                grid[k][j] = grid[i][j]
                grid[i][j] = tmp 
                k += 1
            elif c == '#':
                k = i+1

def shift_left(grid: list[list[chr]]):
    for i in range(len(grid)):
        k = 0 
        for j in range(len(grid[0])):
            c = grid[i][j]
            if c == 'O':
                tmp = grid[i][k]
                grid[i][k] = grid[i][j]
                grid[i][j] = tmp 
                k += 1
            elif c == '#':
                k = j+1

def shift_down(grid: list[list[chr]]):
    grid.reverse()
    shift_up(grid)
    grid.reverse()

def shift_right(grid: list[list[chr]]):
    for line in grid:
        line.reverse()
    shift_left(grid)
    for line in grid: 
        line.reverse()

def print_grid(grid: list[list[chr]]):
    lines = []
    for line in grid:
        lines.append(''.join(line))
    print('\n'.join(lines))

def hash_grid(grid: list[list[chr]]):
    lines = []
    for line in grid:
        lines.append(''.join(line))
    return '\n'.join(lines)

def do_cycle(grid: list[list[chr]]):
    shift_up(grid)
    shift_left(grid)
    shift_down(grid)
    shift_right(grid)

def compute_load(grid: str):
    grid = grid.split('\n')
    res = 0
    for i, line in enumerate(grid):
        res += (len(grid[0]) - i) * line.count('O')
    print(res)


def solve(grid: list[str]):
    cycle_start = 0
    cycle_len = 0
    N = 1000000000

    prev = {hash_grid(grid): 0} 
    for i in range(1, N + 1):
        print(f"---- Cycle {i} -----")
        do_cycle(grid)
        #print_grid(grid)

        h = hash_grid(grid)
        if h in prev:
            cycle_start = prev[h]
            cycle_len = i - prev[h]
            print(f"Found repeated cycle start: {cycle_start}, cycle len: {cycle_len}")
            break
        prev[h] = i

    
    end_i = (N - cycle_start) %  cycle_len + cycle_start  
    for key, i in prev.items():
        if i == end_i: 
            compute_load(key)
            break

    

def main():
    input = read_input()
    solve(input)

if __name__ == "__main__":
    main()