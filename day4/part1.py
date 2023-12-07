import sys

def read_input():
    ret = []
    for line in sys.stdin:
        ret.append(line.rstrip())
    return ret 

def str_to_list(input: str) -> list[int]:
    input = input.strip(' ')
    return [int(v) for v in input.split(' ') if len(v)]

def solve(cards: list[str]):
    sum = 0 
    for card in cards:
        _, data = card.split(":")
        winning_vals, scratched = map(str_to_list, data.split("|")) 
        winning_vals = set(winning_vals)

        winners = [ v for v in scratched if v in winning_vals]
        if winners: 
            sum += 1 << len(winners) - 1
    print (sum)

def main():
    input = read_input()
    solve(input)

if __name__ == "__main__":
    main()