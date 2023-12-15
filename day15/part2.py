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
    boxes = [{} for _ in range(256)]
    for cmd in cmds:
        if '-' in cmd: 
            name = cmd.split('-')[0]
            box = boxes[compute_hash(name)]
            if name in box: 
                box.pop(name)
        elif '=' in cmd: 
            name, f = cmd.split('=') 
            boxes[compute_hash(name)][name] = int(f)
        # print([box for box in boxes if len(box) > 0])
    sum = 0
    for i, box in enumerate(boxes): 
        for j, name in enumerate(box):
            sum += (i+1)*(j+1)*box[name]
    print(sum)

def main():
    cmds = read_input()
    solve(cmds)

if __name__ == "__main__":
    main()