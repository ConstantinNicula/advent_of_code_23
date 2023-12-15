import sys

def read_input():
    ret = []
    line = sys.stdin.readline().strip()
    for cmd in line.split(','):
        ret.append(cmd)
    return ret

def compute_hash(s: str) -> int:
    acc = 0
    for c in s:
        acc += ord(c)
        acc = acc * 17
        acc = acc % 256

    return acc

def solve(cmds:str):
    sum = 0
    for cmd in cmds:
        sum += compute_hash(cmd)
    print(sum)

def main():
    cmds = read_input()
    solve(cmds)

if __name__ == "__main__":
    main()