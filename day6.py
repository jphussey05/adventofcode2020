def get_intersection(group):
    if len(group) == 1:
        return len(group[0])
    else:
        yeses = set(group[0])
        for g in group[1:]:
            yeses = yeses.intersection(g)
        return len(yeses)


with open('day6.txt') as fin:
    contents = [line.strip() for line in fin.readlines()]

answers = []
total = 0
cur_group = []

for row in contents:
    if row == '':
        # total += len(set(answers))
        total += get_intersection(cur_group)
        cur_group = []
    else:
        cur_group.append(row)
        # answers.extend(list(row))

total += get_intersection(cur_group)
print(total)