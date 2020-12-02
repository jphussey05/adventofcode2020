from pprint import pprint

with open('day2.txt') as fin:
    contents = fin.readlines()



# parse input and clean it all up
parsed = []

for line in contents:
    req, pw = line.strip().split(':')
    rng, c = req.split()
    low, high = rng.split('-')
    
    parsed.append((int(low), int(high), c, pw.strip()))

pprint(parsed)

cnt = 0
for item in parsed:
    if item[2] not in item[3]:
        continue    
    # PART I
    # elif item[0] <= item[3].count(item[2]) <= item[1]:  
    #     cnt += 1
    #     print(f'{item} works!')
    # PART II
    else:
        two_positions = item[3][item[0] - 1] + item[3][item[1] - 1]
        if two_positions.count(item[2]) == 1:
            cnt += 1
            print(f'{item} works!')

print(f'Total valid passwords is {cnt}')