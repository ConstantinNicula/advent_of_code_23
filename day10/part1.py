import sys
from collections import deque

def read_input() -> list[str]:
    grid = []
    for line in sys.stdin: 
        grid.append(line.strip())
    return grid


def solve(grid: list[str]):
    pipes = {}
    start_loc = None 
    for i, row in enumerate(grid):
        for j, tile in enumerate(row):
            if tile == '|':
                pipes[(i, j)] = [(i-1, j), (i+1, j)]
            elif tile == '-':
                pipes[(i, j)] = [(i, j-1), (i, j+1)]
            elif tile == 'L':
                pipes[(i, j)] = [(i-1, j), (i, j+1)]
            elif tile == 'J':
                pipes[(i, j)] = [(i-1, j), (i, j-1)]
            elif tile == '7':
                pipes[(i, j)] = [(i+1, j), (i, j-1)]
            elif tile == 'F':
                pipes[(i, j)] = [(i+1, j), (i, j+1)]
            elif tile == 'S':
                start_loc = (i, j) 
    assert start_loc is not None
    
    # link start loc 
    i, j = start_loc
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    start_links = []
    for di, dj in dirs: 
       nb = (i + di, j + dj)
       if nb in pipes and start_loc in pipes[nb]:
           start_links.append(nb) 
    pipes[start_loc] = start_links

    # find cycle length 
    remaining = deque([start_loc])
    visited = {start_loc}
    steps = 0
    while remaining:
        n = len(remaining)
        for i in range(n):
            node = remaining.popleft()
            for adj in pipes[node]:
                if adj not in visited:
                    visited.add(adj)
                    remaining.append(adj)
        if remaining: 
            steps+=1
    print(steps)

def main():
    grid = read_input()
    solve(grid)


if __name__ == "__main__":
    main()