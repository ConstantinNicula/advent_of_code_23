import sys 
import networkx as nx
from collections import deque

def read_input():
    adj = {}
    for line in sys.stdin:
       src, dests = line.strip().split(': ')
       for dest in dests.split(' '):
            if src in adj:
                adj[src].append(dest)
            else: 
                adj[src] = [dest]
    return adj

def edge(node1, node2):
    return (node1, node2) if node1 < node2 else (node2, node1)

def flood_fill(st, adj, edge_count):
    visited = {st}
    active = deque([st])

    while len(active):
        n = len(active)
        for _ in range(n):
            cnode = active.popleft()
            for nnode in adj[cnode]:
                e = edge(cnode, nnode)
                if nnode not in visited:
                    edge_count[e] = edge_count[e] + 1 if e in edge_count else 1
                    active.append(nnode)
                    visited.add(nnode)

def solve(adj):
    G = nx.Graph()
    for src in adj: 
        for dest in adj[src]:
            G.add_edge(src, dest)
    
    rem_edges = nx.minimum_edge_cut(G)
    for src, dest in rem_edges: 
        G.remove_edge(src, dest)
    cc = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    print(cc[0] * cc[1])
    
def main():
    adj = read_input()
    solve(adj)

if __name__ == "__main__":
    main()