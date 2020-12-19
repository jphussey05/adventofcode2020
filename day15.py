from collections import Counter, defaultdict
from time import time

def listRightIndex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1

if __name__ == "__main__":
    with open('day15.txt')  as fin:
        contents = [(int(line)) for line in fin.read().split(',')]


    turn_cnt = 1
    number_spoken = defaultdict(list) # populate with None to offset by 1
    number_counter = Counter()

    for num in contents:
        number_spoken[num].append(turn_cnt)
        number_counter[num] += 1
        last_num = num
        turn_cnt +=1


    while turn_cnt <= 30000000:
        # print(f'Turn {turn_cnt}')
        if number_counter[last_num] == 1:  #last number was first time it was seen
            # print(f'  {last_num} has only been seen once, appending 0')
            number_spoken[0].append(turn_cnt)
            number_counter[0] += 1
            last_num = 0
        else:
            most_recent = number_spoken[last_num][-2]
            diff = turn_cnt - 1 - most_recent
            number_spoken[diff].append(turn_cnt)
            number_counter[diff] += 1
            # print(f'  {last_num} was last seen on turn {most_recent}, appending {diff}')

            last_num = diff
        
        turn_cnt +=1
            

for k, v in number_spoken.items():
    if 30000000 in v:
        print(k)