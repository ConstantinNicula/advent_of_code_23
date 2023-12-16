import sys
from collections import deque

def read_input():
    out = []
    for line in sys.stdin: 
        out.append(line.rstrip())
    return out

def is_out_of_bounds(cpos: tuple[int, int], grid: list[str]): 
    return cpos[0] < 0 or cpos[1] < 0 or cpos[0] >= len(grid) or cpos[1] >= len(grid[0])

dir_vecs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
RIGHT, LEFT, UP, DOWN = (0, 1, 2, 3) 


def traverse(grid: list[str], start_state: tuple[tuple[int, int], int]):
    # state = position & direction
    visited = {start_state}
    active = deque([start_state])

    while len(active):
        n = len(active)
        for _ in range(n):
            cpos, cdir = active.popleft()
            if is_out_of_bounds(cpos, grid):
                continue

            c = grid[cpos[0]][cpos[1]]
           
            # beam splitter
            if c == '|' and (cdir == LEFT or cdir == RIGHT):
                split_dirs = [UP, DOWN]
                for split_dir in split_dirs:
                    dir_vec = dir_vecs[split_dir]

                    split_s = ((cpos[0] + dir_vec[0], cpos[1]+ dir_vec[1]), split_dir)  
                    if split_s not in visited and not is_out_of_bounds(split_s[0], grid):
                        visited.add(split_s)
                        active.append(split_s)
            elif c == '-' and (cdir == UP or cdir == DOWN):
                split_dirs = [LEFT, RIGHT]
                for split_dir in split_dirs:
                    dir_vec = dir_vecs[split_dir]

                    split_s = ((cpos[0] + dir_vec[0], cpos[1]+ dir_vec[1]), split_dir)  
                    if split_s not in visited and not is_out_of_bounds(split_s[0], grid):
                        visited.add(split_s)
                        active.append(split_s)
            # mirror \ 
            elif c == '\\':
                mirror_dirs = {RIGHT: DOWN, LEFT: UP, UP: LEFT, DOWN: RIGHT} 
                dir_vec = dir_vecs[mirror_dirs[cdir]]
                mirror_s = ((cpos[0] + dir_vec[0], cpos[1] + dir_vec[1]), mirror_dirs[cdir])
                if mirror_s not in visited and not is_out_of_bounds(mirror_s[0], grid): 
                    visited.add(mirror_s)
                    active.append(mirror_s)
            elif c == '/':
                mirror_dirs = {RIGHT: UP, LEFT: DOWN, UP: RIGHT, DOWN: LEFT} 
                dir_vec = dir_vecs[mirror_dirs[cdir]]
                mirror_s = ((cpos[0] + dir_vec[0], cpos[1] + dir_vec[1]), mirror_dirs[cdir])
                if mirror_s not in visited and not is_out_of_bounds(mirror_s[0], grid): 
                    visited.add(mirror_s)
                    active.append(mirror_s) 
            # empty space
            else: 
                dir_vec = dir_vecs[cdir]
                nstate = ((cpos[0] + dir_vec[0], cpos[1] + dir_vec[1]), cdir)
                if nstate not in visited and not is_out_of_bounds(nstate[0], grid):
                    visited.add(nstate)
                    active.append(nstate)

    unique_pos = set()
    for p, d in visited:
        unique_pos.add(p)
    return len(unique_pos)

def solve(grid: list[str]): 
    best = 0
    # top 
    for i in range(len(grid[0])):
        best = max(best, traverse(grid, ((0, i), DOWN))) 
    # down 
    for i in range(len(grid[0])):
        best = max(best, traverse(grid, ((len(grid)-1, i), UP))) 

    # left 
    for i in range(len(grid)):
        best = max(best, traverse(grid, ((i, 0), RIGHT)))

    # right 
    for i in range(len(grid)):
        best = max(best, traverse(grid, ((i, len(grid[0])-1), LEFT)))

    print(best)


def main():
    grid = read_input()
    solve(grid)

if __name__ == "__main__":
    main()