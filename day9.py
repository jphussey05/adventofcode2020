from collections import deque
from itertools import combinations


def parse_list(window, next_num):
    combos = list(combinations(window, 2))
    for c in combos:
        if c[0] + c[1] == next_num:
            return True
    
    return False


def find_set(contents, weak_num):
    for i, x in enumerate(contents):
        weak_set = [x]
        for y in range(i+1, len(contents)):
            weak_set.append(contents[y])
            if sum(weak_set) == weak_num:
                return min(weak_set) + max(weak_set)
            elif sum(weak_set) > weak_num:
                break
            else:
                continue
    

if __name__ == "__main__":
    
    with open('day9.txt') as fin:
        contents = [int(line.strip()) for line in fin.readlines()]
    
    preamble_size = 25  
    window = deque(contents[:preamble_size])
        
    for next_num in contents[preamble_size:]:
        if parse_list(window, next_num):
            window.popleft()
            window.append(next_num)
        else:
            print(f'{next_num} was not the sum of two numbers in the window.')
            weak_num = next_num
            print(find_set(contents, weak_num))
            break 