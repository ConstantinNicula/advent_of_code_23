import sys
import os
from collections import deque

sys.setrecursionlimit(50000)

def read_input() -> list[str]:
    grid = []
    for line in sys.stdin: 
        grid.append(line.strip())
    return grid

def get_valid_nbs(pos: tuple[int, int], grid: list[str] ) -> list[tuple[int, int]]:
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    valid = []
    for dir in dirs:
        ni, nj = pos[0] + dir[0], pos[1] + dir[1]
        if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
            continue
        tile = grid[ni][nj]
        if tile == '#':
            continue
        valid.append((ni, nj)) 
    return valid


def get_junctions(grid: list[str]):
    w, h = len(grid[0]), len(grid)
    junctions = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != '#' and len(get_valid_nbs((i, j), grid)) >= 3:
                junctions.append((i, j))
    return junctions

def find_connected(st: tuple[int, int], nodes: list[tuple[int, int]], grid: list[str]): 
    visited = set([st])
    adj = []

    cnt = 1
    active = deque([st])
    while len(active):
        n = len(active)
        for _ in range(n):
            cpos = active.popleft()
            nbs = get_valid_nbs(cpos, grid)
            for npos in nbs:
                if npos in visited: 
                    continue

                visited.add(npos)
                if npos in nodes:
                    adj.append((npos, cnt))                    
                    continue  
                active.append(npos)
        cnt += 1
    return adj

# brute force search
def max_path(pos: tuple[int, int], adj: dict, visited: set) -> int:
    if len(adj[pos]) == 0:
        return 0
    
    dist = -1 # invalid path (not ending at exit) 
    visited.add(pos)
    nbs = adj[pos]
    for npos, d in nbs:
        if npos not in visited:
            rem_path = max_path(npos, adj, visited)
            if rem_path >= 0:
                dist = max(dist, d + rem_path)
    visited.remove(pos)
    return dist


def solve(grid: list[str]):
    DEBUG = "DEBUG" in os.environ

    st, end = (0, 1), (len(grid)-1, len(grid[0])-2)
    
    # reduce grid
    nodes = get_junctions(grid)
    nodes.append(st)
    nodes.append(end)

    adj = {}
    for node in nodes: 
        adj[node] = find_connected(node, nodes, grid)
    adj[end] = []

    visited = set([])
    print(max_path(st, adj, visited))

def main():
    grid = read_input()
    solve(grid)

if __name__ == "__main__":
    main()