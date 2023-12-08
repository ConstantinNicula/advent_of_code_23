import sys
import re

def read_input() -> tuple[str, dict]:
    seq = sys.stdin.readline().rstrip()
    sys.stdin.readline() # skip next line
    
    adj = {}
    for line in sys.stdin:
        match = re.match(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line)
        st, left, right = match.groups()
        adj[st] = (left, right)
    return seq, adj 

def solve(seq: str, adj: dict):
    node = "AAA"
    step = 1 
    while True: 
        cur_move = seq[(step - 1) % len(seq)]
        next_node = adj[node][0] if cur_move == "L" else adj[node][1] 

        if next_node == "ZZZ":
            print(step)
            return 
        node = next_node
        step += 1 

def main():
    sequence, adj = read_input()
    print(sequence)
    solve(sequence, adj)

if __name__ == "__main__":
    main()