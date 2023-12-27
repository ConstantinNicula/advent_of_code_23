import sys 
import numpy as np
import z3

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

def solve(pos: np.ndarray, vel: np.ndarray): 
    N = len(pos)
    N = 10
    vx, vy, vz = z3.Real('vx'), z3.Real('vy'), z3.Real('vz')
    px, py, pz = z3.Real('px'), z3.Real('py'), z3.Real('pz')
    t = [z3.Real(f't{i}') for i in range(N)] 
    solver = z3.Solver()
    for i in range(N):
        solver.add( px + vx * t[i] - pos[i][0] - vel[i][0] * t[i] == 0)
        solver.add( py + vy * t[i] - pos[i][1] - vel[i][1] * t[i] == 0)
        solver.add( pz + vz * t[i] - pos[i][2] - vel[i][2] * t[i] == 0)
        print(i)
    res = solver.check() 
    M = solver.model()
    print(M)
    print(M[px], M[py], M[pz])
    print(M[px] + M[py] + M[pz])
    pass

def main():
    pos, vel  = read_input()
    solve(pos, vel)

if __name__ == "__main__":
    main()