from pprint import pprint

def parse_contents(contents):
    if 'no other' in contents:
        return None
    else:
        items = contents.split(', ')
        return [(item.split()[0], ' '.join(item.split()[1:-1])) for item in items]
           

def bag_search(rule_dict, bag_list, target):
    # root is the tuple of the bag being searched
    # target is the shiny gold bag
    print(f'-----received {bag_list}')
    root = bag_list.pop(0)
    print(f'  Root is {root}')
    if rule_dict[root] == None:
        print(f'  No children')
        return 0
    else:
        for sub_bag in rule_dict[root]:
            print(f'  Checking {sub_bag[1]} against {target}')
            if sub_bag[1] == target: # bag contains it directly
                return 1
            else:  # add sub bag to list for recursive search
                print(f'  {sub_bag} does not contain directly, adding to list')
                bag_list.append(sub_bag[1])
        
        print(f'Calling recurisve with {bag_list}')
        return bag_search(rule_dict, bag_list, target)
            

with open('day7.txt') as fin:
    rules = [line.strip() for line in fin.readlines()]

rule_dict = {}
for rule in rules:
    bag, contents = rule.split(' bags contain ')

    rule_dict[bag] = parse_contents(contents)


cnt = 0 
print(rule_dict.keys())
for bag in rule_dict.keys():
    cnt += bag_search(rule_dict, [bag], 'shiny gold')

print(cnt)