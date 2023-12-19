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

def read_input():
    workflows = {} 
    # read rules 
    for line in sys.stdin:
        if line == "\n":
            break
        
        name, rules, fallback = read_workflow(line)
        workflows[name] = (rules, fallback)
    return workflows

def update_part(part: Part, field: str, value: int):
    if field == 'x':
        return part._replace(x=value)
    if field == 'm':
        return part._replace(m=value)
    if field == 's':
        return part._replace(s=value)
    if field == 'a':
        return part._replace(a=value)


def process_part(wname: str, workflows: dict, p_min: Part, p_max: Part) -> int:
    
    # if not a valid interval
    if p_max.x < p_min.x\
       or p_max.m < p_min.m\
       or p_max.a < p_min.a\
       or p_max.s < p_min.s: 
        return 0 

    if wname == ACCEPTED:
        return (p_max.x - p_min.x + 1)\
              * (p_max.m - p_min.m + 1)\
              * (p_max.a - p_min.a + 1)\
              * (p_max.s - p_min.s + 1)
    elif wname == REJECTED:
        return 0 

    rules, fallback = workflows[wname]
    count = 0
    for rule in rules:
        ref = rule.ref
        if rule.op == GT:
            count += process_part(rule.goto, workflows, update_part(p_min, rule.src, ref+1), p_max) # > -> ref + 1
            p_max = update_part(p_max, rule.src, ref) # <=  -> ref 
        if rule.op == LT: 
            count += process_part(rule.goto, workflows, p_min, update_part(p_max, rule.src, ref-1)) # < -> ref - 1
            p_min = update_part(p_min, rule.src, ref)
    return count + process_part(fallback, workflows, p_min, p_max)        

def solve(workflows: dict):
    count = process_part('in', workflows, Part(1, 1, 1, 1), Part(4000, 4000, 4000, 4000))
    print(f"Total {count}")

def main():
    workflows = read_input()
    solve(workflows)

if __name__ == "__main__":
    main()