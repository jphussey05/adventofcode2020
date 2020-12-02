import time
from itertools import combinations

def forloops(expenses):
    expenses = [int(line.strip()) for line in contents]

    for exp1 in expenses:
        for exp2 in expenses[::-1]:
            for exp3 in expenses:
                if exp1 + exp2 + exp3 == 2020:
                    return exp1 * exp2 * exp3


def combos(expenses):
    expenses = combinations([int(line.strip()) for line in contents], 3)
    for exp in expenses:
        if sum(exp) == 2020:
            return exp[0] * exp[1] * exp[2]

    

with open('day1.txt') as fin:
    contents = fin.readlines()

time_total = 0
for _ in range(1000):

    t1 = time.time()
    forloops(contents)
    t2 = time.time()
    time_total += (t2-t1)

print(f'For loops took an average of {time_total / 1000}')

time_total = 0
for _ in range(1000):
    t1 = time.time()
    combos(contents)
    t2 = time.time()
    time_total += (t2-t1)

print(f'Combinations took an average of {time_total / 1000}')