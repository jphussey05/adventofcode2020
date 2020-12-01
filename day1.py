with open('day1.txt') as fin:
    contents = fin.readlines()

expenses = sorted([int(line.strip()) for line in contents])

for exp1 in expenses:
    for exp2 in expenses[::-1]:
        for exp3 in expenses:
            if exp1 + exp2 + exp3 == 2020:
                hit = exp1, exp2, exp3, exp1 * exp2 * exp3

print(f'Finished and product of {hit[0]} and {hit[1]} and {hit[2]} is {hit[3]}')