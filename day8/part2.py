import sys
import re, math
import functools

def read_input() -> tuple[str, dict]:
    seq = sys.stdin.readline().rstrip()
    sys.stdin.readline() # skip next line
    
    adj = {}
    for line in sys.stdin:
        match = re.match(r"([0-9A-Z]{3}) = \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)", line)
        st, left, right = match.groups()
        adj[st] = (left, right)
    return seq, adj 

def loop_details(start_node: str, seq: str, adj: dict): 
    cycle_start, cycle_length, found_start = 0, 0, False
    cur_node, step = start_node, 1
    while True:
        move = seq[(step-1) % len(seq)]
        next_node = adj[cur_node][0 if move == 'L' else 1]

        # find first target point:
        if next_node[-1] == 'Z':
            if found_start:
                cycle_length = step - cycle_start
                break
            else:
                cycle_start = step
                found_start = True 
        step += 1
        cur_node = next_node
    return cycle_start, cycle_length

def solve(seq: str, adj: dict):
    start_nodes = list(filter(lambda name: name[-1]=='A', adj.keys()))
    cycle_lengths = []
    for node in start_nodes:
        cycle_start, cycle_length = loop_details(node, seq, adj)
        print(cycle_start, cycle_length)
        cycle_lengths.append(cycle_length)

    gcd = cycle_lengths[0]
    for cl in cycle_lengths:
        gcd = math.gcd(gcd, cl)

    res = 1
    for cl in cycle_lengths:
        res = res * cl 
    res /= gcd**(len(cycle_lengths)-1)
    print (f"{res:f}")

def main():
    sequence, adj = read_input()
    print(len(sequence)) 
    solve(sequence, adj)

if __name__ == "__main__":
    main()