import sys 
import re

def to_int_arr(s: str): 
    return [int(v) for v in s.split(",") if v]    


def read_input():
    pos, vel = [], []
    for line in sys.stdin: 
        ps, vs= line.split("@")
        px, py, pz = to_int_arr(ps)
        vx, vy, vz = to_int_arr(vs)

        pos.append((px, py, pz))
        vel.append((vx, vy, vz))

    return pos, vel

MIN = 200000000000000
MAX = 400000000000000

# MIN, MAX = 7, 27

def intersect(p1, v1, p2, v2):
    n = (v2[1], -v2[0])
    d = n[0] * p2[0] + n[1]* p2[1]

    #(p1 + v1 * t) * n = d 
    # t = (d - p1 *n) / v1*n
    v1dot = n[0] * v1[0] + n[1] * v1[1]
    p1dot = n[0] * p1[0] + n[1] * p1[1]

    # paths are parallel
    if v1dot == 0: 
        return False
    t = (d - p1dot)/v1dot
    
    # paths intersect in the past
    if t < 0: 
        return False 

    pi = (p1[0] + v1[0] * t, p1[1] + v1[1] * t)    
    return MIN <= pi[0] <= MAX and MIN <= pi[1] <= MAX

def solve(pos: list[tuple[int]], vel: list[tuple[int]]): 
    cnt = 0
    for i in range(len(pos)-1):
        for j in range(i, len(pos)):
            cnt += intersect(pos[i], vel[i], pos[j], vel[j]) and \
                    intersect(pos[j], vel[j], pos[i], vel[i])
    print(cnt)

def main():
    pos, vel  = read_input()
    solve(pos, vel)

if __name__ == "__main__":
    main()