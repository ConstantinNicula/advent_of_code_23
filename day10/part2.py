import sys
from collections import deque

def read_input() -> list[str]:
    grid = []
    for line in sys.stdin: 
        grid.append([*line.strip()])
    return grid


def get_neighbors(grid, i, j):
    if i < 0 or j < 0 or \
       i >= len(grid) or j >= len(grid[0]):
       return [] 

    tile, nbs = grid[i][j], []
    if tile == '|':
        nbs = [(i-1, j), (i+1, j)]
    elif tile == '-':
        nbs = [(i, j-1), (i, j+1)]
    elif tile == 'L':
        nbs = [(i-1, j), (i, j+1)]
    elif tile == 'J':
        nbs = [(i-1, j), (i, j-1)]
    elif tile == '7':
        nbs = [(i+1, j), (i, j-1)]
    elif tile == 'F':
        nbs = [(i+1, j), (i, j+1)]
    return nbs


def flood_fill(trace_grid, i, j, val):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if trace_grid[i][j] != -1:
        return 0
    
    remaining = deque([(i, j)])
    trace_grid[i][j] = val 
    cnt = 1
    while remaining:
        ni, nj = remaining.popleft() 
        for di, dj in dirs:
            ai, aj = ni + di, nj + dj
            if ai < 0 or aj < 0 or ai >= len(trace_grid) or aj >= len(trace_grid[0]):
                continue    
            if trace_grid[ai][aj] == -1:
                trace_grid[ai][aj] = val
                remaining.append((ai, aj))
                cnt += 1
    return cnt 

def get_perp(p1, p2):
    di, dj = (p2[0] - p1[0], p2[1]- p1[1])
    return (-dj, di)


def solve(grid: list[str]):
    # find start location 
    start_loc = None
    start_adj = []
    for i, row in enumerate(grid):
        for j, tile in enumerate(row): 
            if tile != 'S':
                continue
            start_loc = (i, j)
            
            if start_loc in get_neighbors(grid, i-1, j):
                start_adj.append((i-1, j))
            if start_loc in get_neighbors(grid, i+1, j):
                start_adj.append((i+1, j))

            if start_loc in get_neighbors(grid, i, j-1):
                start_adj.append((i, j-1))
            if start_loc in get_neighbors(grid, i, j+1):
                start_adj.append((i, j+1))
            break

    # -1 nothing, 0 edge, 1-2 outside inside
    trace_grid = [[-1]*(len(grid[0])+2) for _ in range(len(grid)+2)]
    trace_grid[start_loc[0]+1][start_loc[1]+1] = 0   

    # find cycle length 
    visited = {start_loc, start_adj[0]}
    visited_in_order = [start_loc]
    remaining = deque([start_adj[0]])
    while remaining:
        n = len(remaining)
        for i in range(n):
            node = remaining.popleft()
            visited_in_order.append(node)
            trace_grid[node[0]+1][node[1]+1] = 0
            for adj in get_neighbors(grid, node[0], node[1]):
                if adj not in visited:
                    visited.add(adj)
                    remaining.append(adj)

    print(len(visited)//2)

    # start parsing again filling inside and out with different colors
    sum_ones, sum_twos = 0, 0
    visited_in_order.append(visited_in_order[0])

    for i in range(len(visited_in_order) - 1):
        pi, pj = visited_in_order[i]

        fni, fnj = get_perp(visited_in_order[i+1], visited_in_order[i]) # forward normal
        bni, bnj = get_perp(visited_in_order[i], visited_in_order[i-1]) # backward normal 
        cni, cnj = fni + bni, fnj + bnj # sum of normals

        if fni == bni and fnj == bnj:
            sum_ones += flood_fill(trace_grid, pi + 1 + fni, pj + 1 + fnj, 1)
            sum_twos += flood_fill(trace_grid, pi + 1 - fni, pj + 1 - fnj, 2)
        else: 
            sum_ones += flood_fill(trace_grid, pi + 1 + fni, pj + 1 + fnj, 1)
            sum_ones += flood_fill(trace_grid, pi + 1 + cni, pj + 1 + cnj, 1)
            sum_ones += flood_fill(trace_grid, pi + 1 + bni, pj + 1 + bnj, 1)

            sum_twos += flood_fill(trace_grid, pi + 1 - fni, pj + 1 - fnj, 2)
            sum_twos += flood_fill(trace_grid, pi + 1 - cni, pj + 1 - cnj, 2)
            sum_twos += flood_fill(trace_grid, pi + 1 - bni, pj + 1 - bnj, 2)


    # sanity check 
    sentinel_pts = len(trace_grid) * len(trace_grid[0]) - len(grid)*len(grid[0])
    if trace_grid[0][0] == 1: 
        print(f"inside {sum_twos}, outside {sum_ones-sentinel_pts}, edge {len(visited)}")
        print(f"total {sum_twos + sum_ones -sentinel_pts + len(visited)}, theoretical {len(grid) * len(grid[0])}")
    else: 
        print(f"inside {sum_ones}, outside {sum_twos-sentinel_pts}, edge {len(visited)}")
        print(f"total {sum_twos + sum_ones -sentinel_pts + len(visited)}, theoretical {len(grid) * len(grid[0])}")

def main():
    grid = read_input()
    solve(grid)


if __name__ == "__main__":
    main()