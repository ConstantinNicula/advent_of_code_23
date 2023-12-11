import sys

def read_input() -> list[list[chr]]:
    ret = []
    for line in sys.stdin:
        ret.append([*line.rstrip()])
    return ret

def find_empty(m: list[list[chr]]):
    empty_rows = [] 
    for row in m: 
        if row.count('.') == len(row):
            empty_rows.append(True)
        else: 
            empty_rows.append(False) 

    empty_cols = []
    for col in zip(*m):
        if col.count('.') == len(col):
            empty_cols.append(True)
        else:
            empty_cols.append(False) 

    return empty_rows, empty_cols

def solve(m: list[list[chr]]):
    # expand map
    er, ec = find_empty(m) 

    # find stars 
    stars = []
    for i, row in enumerate(m):
        for j, tile in enumerate(row):
            if tile == '#':
                stars.append((i, j)) 

    # compute min distances 
    sum = 0
    mult = 1000000
    for i in range(len(stars) - 1):
        for j in range(i + 1 , len(stars)):
            si, sj = stars[i]
            ti, tj = stars[j]

            # put them in the right order
            if si > ti: si, ti = (ti, si)
            if sj > tj: sj, tj = (tj, sj)

            # count empty between
            emp_i = er[si:ti].count(True)
            emp_j = ec[sj:tj].count(True)
            
            # compute distance 
            dist = abs(ti - si + emp_i * (mult-1)) + abs(tj - sj + emp_j * (mult-1))
            sum += dist
    
    print(sum)

def main(): 
    input = read_input()
    solve(input)

if __name__ == "__main__":
    main()