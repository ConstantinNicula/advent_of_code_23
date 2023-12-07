import sys
import math

def str_to_int(input: str) -> int:
    input = input.strip(' ')
    return int(''.join(input.split(' ')))

def read_input():
    time = str_to_int(sys.stdin.readline().rstrip().split(':')[1])
    distance = str_to_int(sys.stdin.readline().rstrip().split(':')[1]) 
    return time, distance 

def solve_quadratic(T: int, d: int): 
    dis = T ** 2 - 4 * d
    if dis < 0: 
        return ()
    if dis == 0: 
        return (T/2,) 

    dis = math.sqrt(dis)
    t1 = int(math.floor((T - dis)/2))
    t2 = int(math.floor((T + dis)/2))

    if t1 * (T - t1) <= d: t1 += 1
    if t2 * (T - t2) <= d: t2 -= 1

    return t1, t2    


def solve(input):
    time, distance = input
    roots = solve_quadratic(time, distance)
    if len(roots) == 1: 
        print(1)
    if len(roots) == 2: 
        print(roots[1] - roots[0] + 1)

def main():
    input = read_input()
    solve(input)

if __name__ == "__main__":
    main()