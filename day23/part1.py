import sys
from collections import deque

sys.setrecursionlimit(5000)

def read_input() -> list[str]:
    grid = []
    for line in sys.stdin: 
        grid.append(line.strip())
    return grid

def get_valid_nbs(pos: tuple[int, int], grid: list[str] ) -> list[tuple[int, int]]:
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    slopes = { '<': (0, -1), '>': (0, 1), 'v': (1, 0)}    

    valid = []
    for dir in dirs:
        ni, nj = pos[0] + dir[0], pos[1] + dir[1]
        if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
            continue
        tile = grid[ni][nj]
        if tile == '#':
            continue

        if tile not in slopes or slopes[tile] == dir: 
            valid.append((ni, nj)) 
    return valid


def max_path(pos: tuple[int, int], grid: list[str], visited: set, dist: map ={}) -> int:
    if pos in dist: 
        return dist[pos]
    dist[pos] = 0
    visited.add(pos)
    for npos in get_valid_nbs(pos, grid):
        if npos not in visited:
            dist[pos] = max(dist[pos], max_path(npos, grid, visited, dist))
    visited.remove(pos)
    dist[pos] += 1

    return dist[pos]

def solve(grid: list[str]):
    visited = set([])
    dist = {}
    st = (0, 1)
    print(max_path(st, grid, visited, dist)-1)
    h, w = len(grid), len(grid[0])

def main():
    grid = read_input()
    solve(grid)

if __name__ == "__main__":
    main()