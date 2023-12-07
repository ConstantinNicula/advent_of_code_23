import sys

class Interval: 
    def __init__(self, start, end):
        self.start = start
        self.end = end 
        self.span = end - start + 1 
    def __repr__(self):
        return f"[{self.start}, {self.end}]"

class IntervalMap: 
    def __init__(self, dest, src, span):
        self.dest_start = dest 
        self.dest_end = dest + span - 1

        self.src_start = src
        self.src_end = src + span - 1
        
        self.span = span

    def __repr__(self):
        return f"[{self.src_start}, {self.src_end}] -> [{self.dest_start, self.dest_end}]"


    def intersect(self, interval: Interval) -> Interval|None: 
        intersect_min = max(interval.start, self.src_start)
        intersect_max = min(interval.end, self.src_end)

        if intersect_max < intersect_min:
            return None
        return Interval(intersect_min, intersect_max)

    def left_disjoint(self, interval: Interval) -> Interval|None:
        if interval.start < self.src_start:
            return Interval(interval.start, min(interval.end, self.src_start - 1))
        return None

    def right_disjoint(self, interval: Interval) -> Interval|None:
        if interval.end > self.src_end:
            return Interval(max(interval.start, self.src_end + 1), interval.end)
        return None

    def map_value(self, v: int) -> int:
        if v >= self.src_start and v <= self.src_end:
            return (v - self.src_start) + self.dest_start 
        return v

    def map_interval(self, interval: Interval) -> Interval:
        return Interval(self.map_value(interval.start), self.map_value(interval.end))  


def skip_line():
    _ = sys.stdin.readline()

def str_to_list(input: str) -> list[int]:
    input = input.strip(' ')
    return [int(v) for v in input.split(' ') if len(v)]

def read_seed_ranges() -> list[Interval]:
    seeds = str_to_list(sys.stdin.readline().rstrip().split(':')[1])
    skip_line()

    ret = [] 
    for st, l in zip(*(iter(seeds), )* 2):
        ret.append(Interval(st, st + l - 1))
    return ret

def read_map() -> list[IntervalMap]:
    ret = []
    skip_line()
    for line in sys.stdin: 
        line_s = line.rstrip()
        if not line_s: break
        dst, src, length = str_to_list(line_s) 
        ret.append(IntervalMap(dst, src, length))
    return ret 

def read_input() -> tuple[list[Interval], list[list[IntervalMap]]]:
    seeds = read_seed_ranges()
    maps, num_maps = [], 7
    for i in range(num_maps):
        maps.append(read_map()) 
    return (seeds, maps) 


def split_and_map_interval(interval: Interval, interval_map: IntervalMap, proc_done: list[Interval], proc_pending: list[Interval]):
    # common area between interval and interval_map, move to done list 
    intersect = interval_map.intersect(interval)
    if intersect: proc_done.append(interval_map.map_interval(intersect))

    # check left and right disjoint intervals   
    left = interval_map.left_disjoint(interval)
    if left: proc_pending.append(left)

    right = interval_map.right_disjoint(interval)
    if right: proc_pending.append(right)

    # print (interval ,"&", interval_map,"=>", left, intersect, right)


def interval_apply_mapping(interval: Interval, interval_maps: list[IntervalMap]) -> list[Interval]:
    proc_done = []
    proc_pending = [interval]

    for interval_map in interval_maps:
        tmp = []
        for interval in proc_pending: 
            split_and_map_interval(interval, interval_map, proc_done, tmp)
        # print(tmp)
        proc_pending = tmp

    proc_done.extend(proc_pending)
    return proc_done 

def interval_apply_mapping_repeated(interval: Interval, n_interval_maps: list[list[IntervalMap]] ) -> list[Interval]:
    prev = [interval]
    for m in n_interval_maps:
        tmp = []
        for inter in prev:
            tmp.extend(interval_apply_mapping(inter, m))
        prev = tmp
    return prev 


def solve(seeds: list[int], maps: list):
    dest_locs = []
    for i in range(len(seeds)):
        dest_locs.extend(interval_apply_mapping_repeated(seeds[i], maps))

    min_val = min(map(lambda loc_int: loc_int.start, dest_locs))    
    print(min_val)

def main():
    seeds, maps = read_input()
    solve(seeds, maps)

if __name__ == "__main__":
    main()
