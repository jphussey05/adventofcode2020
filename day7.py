debug = False

import sys
from pprint import pprint

print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
def parse_contents(contents):
    if 'no other' in contents:
        return []
    else:
        items = contents.split(', ')
        return [(item.split()[0], ' '.join(item.split()[1:-1])) for item in items]
           

def bag_search(rule_dict, bag_list, target):
    # root is the tuple of the bag being searched
    # target is the shiny gold bag
    if debug:
        print(f'-----received {bag_list}')
    
    if bag_list == []:
        if debug:
            print(f'  Exhausted List')
        return 0
    else:
        root = bag_list.pop(0)
        if debug:
            print(f'  Root is {root} with children {rule_dict[root]}')

        for sub_bag in rule_dict[root]:
            if debug:
                print(f'  Checking {root}"s {sub_bag[1]} against {target}')
            if sub_bag[1] == target: # bag contains it directly
                if debug:
                    print(f'  ***bag contained directly, returning 1')
                return 1
            else:  # add sub bag to list for recursive search
                if debug:
                    print(f'  ***{sub_bag[1]} is not {target}, adding to list')
                bag_list.append(sub_bag[1])
        
        if debug:
            print(f'  ***Calling recurisve with {bag_list}')
        return bag_search(rule_dict, bag_list, target)
            

with open('day7.txt') as fin:
    rules = [line.strip() for line in fin.readlines()]

rule_dict = {}
for rule in rules:
    bag, contents = rule.split(' bags contain ')

    rule_dict[bag] = parse_contents(contents)


cnt = 0 
if debug:
    print(rule_dict.keys())
for bag in rule_dict.keys():
    if bag != 'shiny gold':
        cnt += bag_search(rule_dict, [bag], 'shiny gold')

print(cnt)