import sys
import re
from dataclasses import dataclass

class Brick:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = min(x1, x2)
        self.x2 = max(x1, x2)

        self.y1 = min(y1, y2)
        self.y2 = max(y1, y2)

        self.z1 = min(z1, z2)
        self.zh = max(z1, z2) - self.z1 + 1
        
        self.touching_above = set([]) 
        self.touching_below = set([]) 

    def add_touching_above(self, brick):
        self.touching_above.add(brick)

    def add_touching_below(self, brick):
        self.touching_below.add(brick)

    def move_z(self, new_z1: int):
        self.z1 = new_z1 

    def __repr__(self):
        return f"{self.x1=:}, {self.y1=:} ~ {self.x1=:}, {self.y1=:}, {self.z1=:}, {self.zh=:}\n"

def read_input() -> list[Brick]:
    bricks = []
    for line in sys.stdin:
        m = re.match(r"([\d]+),([\d]+),([\d]+)~([\d]+),([\d]+),([\d]+)", line.strip())
        bricks.append(Brick(*[int(nr) for nr in m.groups()]))
    return bricks

def shift_down(bricks: list[Brick]|set[Brick], dz: int):
    for brick in bricks:
        brick.move_z(dz)

def solve(bricks: list[Brick]):
    pr = lambda i: chr(ord('A') + i)

    # sort on z1 
    bricks = sorted(bricks, key=lambda brick: brick.z1)    

    # hmap stores (z, brick) at location (i, j)
    hmap = {}
    for brick in bricks:
        max_h = 0
        for x in range(brick.x1, brick.x2+1):
            for y in range(brick.y1, brick.y2+1):
                max_h = max(max_h, hmap[(x,y)][0] if (x, y) in hmap else 0)

        # nothing below
        if max_h == 0:
            for x in range(brick.x1, brick.x2+1):
                for y in range(brick.y1, brick.y2+1):
                    hmap[(x, y)] = (brick.zh, brick)
        else:
            for x in range(brick.x1, brick.x2+1):
                for y in range(brick.y1, brick.y2+1):
                    new_h = max_h + brick.zh

                    if (x, y) in hmap:
                        # create links
                        h, below = hmap[(x, y)] 
                        if h == max_h:
                            below.add_touching_above(brick)
                            brick.add_touching_below(below)
                        hmap[(x, y)] = (new_h, brick)
                    else: 
                        hmap[(x, y)] = (new_h, brick)    

    depends = {brick:[] for brick in bricks}
    for brick in bricks:
        for above in brick.touching_above:
            if len(above.touching_below) <= 1:
                depends[brick].append(above)
    
    cnt = 0
    for _, d in depends.items():
        if len(d) == 0:
            cnt += 1

    print(cnt)

def main():
    bricks = read_input()
    solve(bricks)

if __name__ == "__main__":
    main()