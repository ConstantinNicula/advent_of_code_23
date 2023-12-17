import sys
from queue import PriorityQueue

def read_input() ->list[str]:
    grid = []
    for line in sys.stdin:
        grid.append(line.strip())
    return grid

MAX_INT, UNDEF = 2**64, -1
PREV_DIR_VERT, PREV_DIR_HOR, PREV_DIR_NONE = 0, 1, 2

valid_moves = {
    PREV_DIR_NONE: [((-1,0), 3), ((-1,0), 2), ((-1,0), 1), 
                    ((1, 0), 3), ((1, 0), 2), ((1, 0), 1),

                    ((0,-1), 3), ((0,-1), 2), ((0,-1), 1), 
                    ((0, 1), 3), ((0, 1), 2), ((0, 1), 1)],

    PREV_DIR_HOR: [((-1,0), 3), ((-1,0), 2), ((-1,0), 1), 
                    ((1, 0), 3), ((1, 0), 2), ((1, 0), 1)],

    PREV_DIR_VERT: [ ((0,-1), 3), ((0,-1), 2), ((0,-1), 1), 
                    ((0, 1), 3), ((0, 1), 2), ((0, 1), 1)],
}

def get_move_type( move: tuple[tuple[int, int], int]):
    dir, cnt = move
    if dir[0] == 0:
        return PREV_DIR_HOR
    if dir[1] == 0: 
        return PREV_DIR_VERT 
    return PREV_DIR_NONE

def do_move(pos: tuple[int, int], move: tuple[tuple[int, int], int], grid: list[str])-> tuple[tuple[int, int], int]:
    dir, count = move 
    cost = 0
    for _ in range(count):
        npos = (pos[0]+dir[0], pos[1]+dir[1])
        if is_valid_pos(npos, grid):
            pos = npos
            cost += int(grid[pos[0]][pos[1]])
        else:
            break
    return pos, cost

def is_valid_pos(pos: tuple[int, int], grid: list[str]): 
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])



def solve(grid: list[str]):
    dist = [[[MAX_INT, MAX_INT] for _ in range(len(grid[0]))] for _ in range(len(grid))] 
    prev = [[[UNDEF, UNDEF] for _ in range(len(grid[0]))] for _ in range(len(grid))] 
    
    # set starting locations
    dist[0][0][0] = 0 
    dist[0][0][1] = 0

    Q = PriorityQueue()
    Q.put((0, (0, 0), PREV_DIR_VERT))
    Q.put((0, (0, 0), PREV_DIR_HOR))
    
    while not Q.empty():
        _, u, prev_move = Q.get()
        # compute neighbors
        for move in valid_moves[prev_move]:
            v, cost = do_move(u, move, grid)
            if cost == 0: 
                continue
            curr_move = get_move_type(move)

            dist_v = dist[u[0]][u[1]][prev_move] + cost
            if is_valid_pos(v, grid) and dist_v < dist[v[0]][v[1]][curr_move]:
                dist[v[0]][v[1]][curr_move] = dist_v 
                prev[v[0]][v[1]][curr_move] = (u[0], u[1], prev_move)
                Q.put((dist_v, v, curr_move))

    disp = [['.'] * len(grid[0]) for _ in range(len(grid))]
    disp[-1][-1] ='#'

    p = prev[-1][-1][1]
    while p != UNDEF:
        print(p)
        disp[p[0]][p[1]] = '#'
        p = prev[p[0]][p[1]][p[2]]

    for row in disp:
        print(''.join(row))

    for row in dist: 
        print(row)
    print(min(dist[-1][-1]))

def main():
    grid = read_input()
    solve(grid)

if __name__ == "__main__":
    main()