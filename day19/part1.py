import sys
import re
from collections import namedtuple


Rule = namedtuple("Rule", ["src", "op", "ref", "goto"])
Part = namedtuple("Part", ["x", "m", "a", "s"])

GT, LT = '>', '<'
REJECTED, ACCEPTED = 'R', 'A'

def read_workflow(line: str) -> tuple[str, list[Rule], str]:
    name, rules_str = line.rstrip('\n}').split('{')
    
    rules = []
    fallback = None
    for rule_str in rules_str.split(','):
        m = re.match(r"([a-z]+)([<>])([0-9]+):([RAa-z]+)", rule_str)
        if m:
            src, op, ref, goto = m.groups()
            rules.append(Rule(src, op, int(ref), goto)) 
        else: 
            fallback = rule_str
    return name, rules, fallback

def read_part(line:str) -> Part:
    m = re.match(r"{x=([0-9]+),m=([0-9]+),a=([0-9]+),s=([0-9]+)}", line)
    assert m
    return Part(*[int(x) for x in m.groups()])

def read_input():
    workflows = {} 
    # read rules 
    for line in sys.stdin:
        if line == "\n":
            break
        
        name, rules, fallback = read_workflow(line)
        workflows[name] = (rules, fallback)

    parts = []
    for line in sys.stdin:
        parts.append(read_part(line))
    return workflows, parts


def process_part(wname: str, workflows: dict, part: Part) -> bool:
    if wname == ACCEPTED:
        return True
    elif wname == REJECTED:
        return False

    rules, fallback = workflows[wname]
    for rule in rules:
        src = getattr(part, rule.src)
        ref = rule.ref

        if rule.op == GT and src > ref:
            return process_part(rule.goto, workflows, part)

        if rule.op == LT and src < ref: 
            return process_part(rule.goto, workflows, part)

    return process_part(fallback, workflows, part)        

def solve(workflows: dict, parts: list):
    sum = 0
    for part in parts:
        if process_part('in', workflows, part):
            delta = part.x + part.m + part.a + part.s
            print(delta)
            sum += delta
    print(f"Total {sum}")

def main():
    workflows, parts = read_input()
    solve(workflows, parts)

if __name__ == "__main__":
    main()