import sys

def read_input() -> list[list[int]]:
    ret = []
    for line in sys.stdin:
       ret.append(list(map(lambda x: int(x), line.rstrip().split(' '))))
    return ret

def extrapolate(nums: list[int]) -> int:
    sum = nums[-1]
    left = nums
    while len(left) > 1: 
        diff = [] 
        for i in range(len(left) - 1): 
            diff.append(left[i+1] - left[i])
        sum += diff[-1]
        left = diff
    return sum

def solve(input):
    sum = 0
    for line in input:
        line.reverse()
        sum += extrapolate(line)
    print(sum) 

def main():
    input = read_input()
    #print(input)
    solve(input)

if __name__ == "__main__":
    main()