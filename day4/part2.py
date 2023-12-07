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
    multiplier = [1] * len(cards) 
    for i, card in enumerate(cards):
        _, data = card.split(":")
        winning_vals, scratched = map(str_to_list, data.split("|")) 
        winning_vals = set(winning_vals)

        winners = len([ v for v in scratched if v in winning_vals])
        if winners: 
            for off in range(1, winners+1):
                multiplier[i + off] += multiplier[i] 
    res = sum(multiplier)
    print(res)
def main():
    input = read_input()
    solve(input)

if __name__ == "__main__":
    main()