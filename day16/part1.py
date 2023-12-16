import sys
from collections import deque

def read_input():
    out = []
    for line in sys.stdin: 
        out.append(line.rstrip())
    return out

def is_out_of_bounds(cpos: tuple[int, int], grid: list[str]): 
    return cpos[0] < 0 or cpos[1] < 0 or cpos[0] >= len(grid) or cpos[1] >= len(grid[0])


def solve(grid: list[str]):
    dir_vecs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    RIGHT, LEFT, UP, DOWN = (0, 1, 2, 3) 

    # state = position & direction
    cur_state = ((0,0), RIGHT)
    visited = {cur_state}
    active = deque([cur_state])

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

    visited_grid = [ ['.'] * len(grid[0]) for _ in range(len(grid))]
    for p, d in visited:
        visited_grid[p[0]][p[1]] = '#'
    for row in visited_grid:
        print(''.join(row))
    
    unique_pos = set()
    for p, d in visited:
        unique_pos.add(p)
    print(len(unique_pos))


def main():
    grid = read_input()
    solve(grid)

if __name__ == "__main__":
    main()