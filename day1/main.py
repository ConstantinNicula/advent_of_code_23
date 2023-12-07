import re 

def read_input(file_name: str) -> list[str]:
    with open(file_name, 'r') as f:
        return f.readlines() 

def extract_int(line:str):
    line = re.sub(r'[a-z]*', '', line.rstrip()) 
    return int(line[0] + line[-1])

def solve(input: list[str]) -> int:
    ret = []
    for line in input: 
        ret.append(extract_int(line))
    return sum(ret)

def extract_int_part_2(line: str):
    patterns = {
        "one": "1", "two": "2",
        "three": "3", "four": "4",
        "five": "5", "six": "6",
        "seven": "7", "eight" :"8", 
        "nine": "9",
    }

    found = []
    # find digit pattern:
    for pattern in patterns:
        s_idx = 0
        while s_idx < len(line): 
            match = re.search(pattern, line[s_idx:])
            if not match: 
                s_idx = len(line)
                continue
            found.append(( s_idx + match.start(), patterns[pattern]))
            s_idx = s_idx + match.start() + 1 
    for idx, chr in enumerate(line):
        if chr.isdigit():
            found.append((idx, chr))
    
    found.sort()
    return int(found[0][1] + found[-1][1])

def solve_part_2(input:list[str]) -> int:
    ret = []
    for line in input:
        ret.append(extract_int_part_2(line))
    return sum(ret)


if __name__ == "__main__":
    input = read_input("input.txt")
    print(solve(input))
    print(solve_part_2(input))