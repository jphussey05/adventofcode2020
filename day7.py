def parse_contents(contents):
    if 'no other' in contents:
        return []
    else:
        items = contents.split(', ')
        return [[int(item.split()[0]), ' '.join(item.split()[1:-1]), 0] for item in items]
           

def bag_search(rule_dict, bag_list, cur_sum):
    if bag_list == []:            # base case
        return cur_sum
    else:                         # recursive case
        root = bag_list.pop(0)
        for sub_bag in rule_dict[root[0]]:
            cur_sum += sub_bag[0] * root[1] #add the number of bags * the multiplier
            bag_list.append((sub_bag[1], sub_bag[0] * root[1])) # add X sub_bag to list 
        
        return bag_search(rule_dict, bag_list, cur_sum)


if __name__ == "__main__":
    with open('day7.txt') as fin:
        rules = [line.strip() for line in fin.readlines()]

    rule_dict = {}
    for rule in rules:
        bag, contents = rule.split(' bags contain ')
        rule_dict[bag] = parse_contents(contents)

    print(bag_search(rule_dict, [('shiny gold', 1)], 0))