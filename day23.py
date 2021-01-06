from time import time
import array as arr
import numpy as np


global new_cups 

def arrange_final(cups):
    for i in range(len(cups)):
    
        if cups[i] == 1:
            one_idx = i
            break
    
    return cups[one_idx+1], cups[one_idx+2]


def pick_destination(cups, pickup):
    cur = cups[0]
    dst = cur - 1
    
    while dst in pickup or dst == 0:
        dst -= 1
        if dst < 1:
            dst = 1000000
    
    return dst

def move(cups):
    t0 = time()
    
    # get three cups, assume 0 index always current
    pickup = np.empty(shape=3)
    pickup[:] = cups[1:4]

    t1 = time()

    # pick destination cup
    dst = pick_destination(cups, pickup)
    t2 = time()

    dst_idx = np.where(cups == dst)[0][0]

    t3 = time()
   
    cups = np.concatenate((cups[4:dst_idx + 1], pickup[:], cups[dst_idx + 1:], [cups[0]]))

    t4 = time()

    # select new current cup (rebuild list?)
    return (t1-t0, t2-t1, t3-t2, t4-t3, t4-t0), cups
    

def populate_cups(cups):
    max_cup = max(cups)
    for n in range(max_cup + 1, 1000001):
        cups.append(n)
    
    return cups


def print_timings(timings, moves):
    print(f'Average run times by section: ')
    print(f'  pickup extraction: {timings[0]/moves}')
    print(f'  pick_destination: {timings[1]/moves}')
    print(f'  new_cup index: {timings[2]/moves}')
    print(f'  new_cup insertion: {timings[3]/moves}')
    print(f'  total run:  {(timings[4])/moves}')


if __name__ == "__main__":
    t1 = time()
    cups = np.array(populate_cups(list(map(int, '362981754'))))
    new_cups = np.empty(shape=1000000)
    moves = 10000000
    timings = (0,0,0,0,0)

    
    for x in range(moves):
        new_timings, cups = move(cups)
        timings = (
            timings[0] + new_timings[0],
            timings[1] + new_timings[1],
            timings[2] + new_timings[2],
            timings[3] + new_timings[3],
            timings[4] + new_timings[4],
        )
      
    

    n1, n2 = arrange_final(cups)
    t2 = time()
    print(f'-- final --')
    print(f'next 2:  {n1} {n2}')
    print(f'next 2 multiplied: {n1 * n2}')
    print(f'Total Run time: {t2-t1}')
    print_timings(timings, moves)
    print(f'Overhead: {t2-t1-timings[4]}')