import sys
import re

def read_input() -> tuple[str, dict]:
    seq = sys.stdin.readline().rstrip()
    sys.stdin.readline() # skip next line
    
    adj = {}
    for line in sys.stdin:
        match = re.match(r"([0-9A-Z]{3}) = \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)", line)
        st, left, right = match.groups()
        adj[st] = (left, right)
    return seq, adj 

def find_recurring(start_node: str, seq: str, adj: dict):
    cur_node = start_node
    step = 0 

    visited = set()
    print(start_node)
    hit = False
    while True:
        seq_id = (step) %  len(seq)
        move = 0 if seq[seq_id] == 'L' else 1

        next_node = adj[cur_node][move]
        if (next_node, seq_id) in visited:
            if hit:
                print(f"exiting at step {step}")
                break 
            hit = True

        cur_node = next_node
        step += 1      

        if next_node[-1] == 'Z': 
            print(f"hit node {next_node} at step {step}")
            visited.add((next_node, seq_id))


    print (visited)

def solve(seq: str, adj: dict):
    # select all nodes that end with A 
    cur_nodes = list(filter(lambda name: name[-1]=='A', adj.keys()))

    for node in cur_nodes:
        find_recurring(node, seq, adj)

def main():
    sequence, adj = read_input()
    solve(sequence, adj)

if __name__ == "__main__":
    main()