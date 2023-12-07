import sys
import math
def str_to_list(input: str) -> list[int]:
    input = input.strip(' ')
    return [int(v) for v in input.split(' ') if len(v)]

def read_input():
    times = str_to_list(sys.stdin.readline().rstrip().split(':')[1])
    distances = str_to_list(sys.stdin.readline().rstrip().split(':')[1]) 
    return times, distances 

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
    times, distances = input
    prod  = 1 
    for i in range(len(times)): 
        roots = solve_quadratic(times[i], distances[i])
        print(roots)
        if len(roots) == 2: 
            prod *= roots[1] - roots[0] + 1
    print(prod)

def main():
    input = read_input()
    solve(input)

if __name__ == "__main__":
    main()