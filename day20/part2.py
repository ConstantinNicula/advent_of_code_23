import sys 
import re
from enum import Enum
from collections import deque
import math

class CompType(Enum):
    BROADCASTER = 1
    FLIPFLOP = 2
    CONJUNCTION = 3
    OUTPUT = 4

class Broadcaster:
    def __init__(self, name: str, dest: list[str]):
        self.name = name
        self.dest = dest
        self.type = CompType.BROADCASTER

    def attach_inputs(self, src: str):
        return 
    
    def send_pulses(self, src: str, pulse: bool) -> list[tuple[bool, str]]:
        return [(self.name, pulse, dest) for dest in self.dest]

class FlipFlop:
    def __init__(self, name: str, dest: list[str]):
        self.name = name
        self.state = False 
        self.dest = dest
        self.type = CompType.FLIPFLOP

    def attach_inputs(self, src: str):
        return

    def send_pulses(self, src: str, pulse: bool) -> list[tuple[bool, str]]:
        if pulse == True: 
            return []
        # flip internal state
        self.state = not self.state
        return [(self.name, self.state, dest) for dest in self.dest]

class Conjunction: 
    def __init__(self, name: str, dest: list[str]):
        self.name = name
        self.input_states = {} 
        self.dest = dest
        self.state = True
        self.type = CompType.CONJUNCTION
    
    def attach_inputs(self, src: str):
        self.input_states[src] = False

    def send_pulses(self, src: str, pulse: bool) -> list[tuple[bool, str]]:
        self.input_states[src] = pulse
        self.state = not all(self.input_states.values()) 
        return [(self.name, self.state, dest) for dest in self.dest]

class Output: 
    def __init__(self):
        self.high_count = 0
        self.low_count = 0
        self.type = CompType.OUTPUT 
    
    def attach_inputs(self, src:str):
        return 

    def send_pulses(self, src: str, pulse: bool) -> None:
        if pulse:
            self.high_count += 1
        else: 
            self.low_count += 1
        return []

def read_input():
    components = {} 
    for line in sys.stdin:
        m = re.match(r"([%&]*)([a-z]+) -> ([a-z, ]+)", line)
        t, name, dest =  m.groups()
        dest = [s.strip() for s in dest.split(',')]

        if t == '%':
            components[name] = FlipFlop(name, dest)
        elif t == '&':
            components[name] = Conjunction(name, dest)
        elif name == 'broadcaster':
            components[name] = Broadcaster(name,dest)


    # create links where needed 
    outputs = {}   
    for c in components:
        for dest in components[c].dest:
            if dest in components:
                components[dest].attach_inputs(c)
            else: 
                outputs[dest] = Output()
    
    for k, v in outputs.items():
        components[k] = v

    return components, list(outputs.keys())

def solve(components: dict, outputs: list[str]):
    print(components.keys(), outputs)
    N = 1000 * 50

    hist = {}

    for i in range(N):
        ev_queue = deque([('button', False, 'broadcaster')]) 
        while len(ev_queue):
            src, state, to = ev_queue.popleft()
            if to == 'rx':
                for k, v in components[src].input_states.items():
                    if v == True:
                        if k in hist:
                            hist[k].add(i+1)
                        else:
                            hist[k] = set([i+1])
            # print(f"{src} -{'high' if state else 'low'} -> {to}")
            new_evs = components[to].send_pulses(src, state)
            for ev in new_evs:
                ev_queue.append(ev)

        if components[outputs[0]].low_count >= 1:
            print(f"found low in iter{i}")
            break
    
    # this is kind of a hack 
    cl = []
    for k, v in hist.items(): 
        sv = sorted(v)
        cl.append(sv[0])
    print(math.lcm(*cl))

def main():
    components, outputs = read_input()
    solve(components, outputs)

if __name__ == "__main__":
    main()