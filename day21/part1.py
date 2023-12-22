import os
import sys 

START = 'S'
ROCKS = '#'
PLOTS = '.'

def read_input():
    grid = []
    si = None
    for i, line in enumerate(sys.stdin):
        grid.append(line.strip())
        if START in line: 
            si = (i, line.index(START))
    return grid, si

def get_valid_nbs(pos: tuple[int, int], grid: list[str], valid_tiles: list = [START, PLOTS]):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    h, w = len(grid), len(grid[0])
    nbs = []
    for dir in dirs:
        ni, nj = pos[0] + dir[0], pos[1] + dir[1]
        if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] in valid_tiles:
            nbs.append((ni, nj))
    return nbs

def display_reachable(grid: list[str], reachable: set, nbs: set = None):
    h, w = len(grid), len(grid[0])
    out = [['' for _ in range(w)] for _ in range(h)]

    for i, row in enumerate(grid):
        for j, tile in enumerate(row):
            if (i, j) in reachable:
                out[i][j] = 'O'
            elif nbs and (i, j) in nbs:
                out[i][j] = 'X'
            else:
                out[i][j] = tile

    for row in out: 
        print(''.join(row))



def solve(grid: list[str], si: tuple[int, int]):
    DEBUG = 'DEBUG' in os.environ 
    
    N = 64 
    reachable = set([si])
    for i in range(N):
        next_reachable = set([])

        for node in reachable: 
            for nb_node in get_valid_nbs(node, grid):
                next_reachable.add(nb_node)
        
        reachable = next_reachable 
        if DEBUG:
            print(f"---- iter {i:<3} ----")
            display_reachable(grid, reachable)
            print(f"------------------\n")
    print(len(reachable))
def main():
    grid, si = read_input()
    solve(grid, si)

if __name__ == "__main__":
    main()