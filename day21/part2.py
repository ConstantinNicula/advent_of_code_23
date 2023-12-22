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
        ni, nj = (pos[0] + dir[0]), (pos[1] + dir[1])
        if grid[ni%h][nj%w] in valid_tiles:
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

def shift_arr(arr: list, n: int) -> list:
    left = arr[:n]
    right = arr[n:]
    return right + left 

def shift_start_to_origin(grid: list[str], si: tuple[int, int]) -> list[str]:
    # shift up
    grid = shift_arr(grid, si[0])
    # shift left
    grid = [''.join(col) for col in zip(*grid)] 
    grid = shift_arr(grid, si[1])
    grid = [''.join(col) for col in zip(*grid)]
    return grid

def count_in_tiles(reachable: set, h: int, w: int, tile_cnt):
    counts = []
    for i in range(tile_cnt):
        i_st = (i - tile_cnt//2) * h  
        i_en = (i+1-tile_cnt//2) * h

        counts.append([])
        for j in range(tile_cnt):
            j_st = (j - tile_cnt//2) * w  
            j_en = (j+1-tile_cnt//2) * w 

            cnt = 0
            for ri, rj in reachable: 
                if i_st <= ri < i_en and  j_st <= rj < j_en:
                    cnt+=1
            counts[i].append(cnt)
            print(f"{cnt:^5}", end='')
        print()
    s = len(reachable)
    so = sum(counts[tile_cnt//2]) + sum(counts[tile_cnt//2 - 1])
    si = 2 * (counts[tile_cnt//2][tile_cnt//2] + counts[tile_cnt//2][tile_cnt//2-1]) 

    return s, so, si

def solve(grid: list[str], si: tuple[int, int]):
    DEBUG = 'DEBUG' in os.environ 
    print(len(grid), len(grid[0]))
    grid = shift_start_to_origin(grid, si)

    steps = 26501365
    k_bf = 2
    k_fast = steps // len(grid) - k_bf 

    # do k_bf iterations 
    rem =  steps % len(grid)
    N =  len(grid)* k_bf + rem 
    reachable = set([(0,0)])
    for i in range(N):
        next_reachable = set([])
        for node in reachable: 
            for nb_node in get_valid_nbs(node, grid):
                next_reachable.add(nb_node)
        reachable = next_reachable 

    s, so, si = count_in_tiles(reachable, len(grid), len(grid[0]), 8)
    
    # do fast iters 
    for i in range (k_fast):
        s+= so + si * (i+1) 
    print(s, si, so) 

def hack_solve():
#   0    0    0    0    0    0    0    0  
#   0    0    0   887  942   0    0    0  
#   0    0   887 6433 6445  942   0    0  
#   0   887 6433 7363 7353 6445  942   0  
#   0   935 6457 7353 7363 6482  970   0  
#   0    0   935 6457 6482  970   0    0  
#   0    0    0   935  970   0    0    0  
#   0    0    0    0    0    0    0    0
    k = 26501365 // 131 - 2 # already did 2 iters
    s = sum([887, 942, 
             887, 6433, 6445, 942, 
             887, 6433, 7363, 7353, 6445, 942, 
             935, 6457, 7353, 7363, 6482, 970, 
             935 ,6457,6482 ,970,
             935, 970
             ]) 
    
    so = sum ([887, 6433, 7363, 7353, 6445, 942, 
             935, 6457, 7353, 7363, 6482, 970 ])
    si = sum ([7363, 7353,
              7353, 7363,])
    for i in range (k):
        s+= so + si * (i+1) 
    print(s, si, so) 

def main():
    grid, si = read_input()
    hack_solve()
    solve(grid, si)

if __name__ == "__main__":
    main()