import sys 

def read_input() -> list[tuple[str, int, str]]:
    ret = []
    for line in sys.stdin:
        cmd, cnt, color = line.strip().split(' ')
        ret.append((cmd, int(cnt), color))
    return ret

def solve(instr: list[tuple[str, int, str]]):
    dirs = { 'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    pos = [(100000, 10000)]
    cx, cy = pos[0]
    per = 0
    for cmd, cnt, _ in instr:
        dx, dy = dirs[cmd]
        cx = cnt * dx + cx
        cy = cnt * dy + cy 
        pos.append((cx, cy))
        per += cnt

    area = 0
    for i in range(len(pos)-1):
        p1, p2 = pos[i], pos[i+1]
        
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        delta = 0
        if dx > 0:
            delta = -(abs(dx)) * (abs(p1[1]))
        else: 
            delta =  (abs(dx)) * (abs(p1[1]))
        area += delta
    
    print(abs(area) + per//2 +1)
def main():
    instr = read_input()
    solve(instr)

if __name__ == "__main__":
    main()