from anytree import AnyNode, RenderTree
from collections import Counter


def get_valids(contents, jolts):
    nexts = []
    for c in contents:
        if c == jolts:
            continue
        elif c <= jolts + 3:
            nexts.append(c)
        else:
            return nexts
    
    return nexts


def build_tree(parent, contents, jolts):
    if contents:
        nexts = get_valids(contents, jolts)
        if nexts:
            parent.children = [AnyNode(id=child) for child in nexts]
            for child in parent.children:
                new_jolts = child.id
                start_idx = contents.index(child.id) + 1
                build_tree(child, contents[start_idx:], new_jolts)
    else:
        return

def count_the_shit(jolts):
    max_jolts = jolts[-1] + 3
    jolts.append(max_jolts)  # add the last value
    jolt_cntr = Counter([0]) # create counter with a single occurrence of 0

    for jolt in jolts:
        print(f'Jolt is {jolt}')
        jolt_cntr[jolt] = sum([
            jolt_cntr[jolt - 1], 
            jolt_cntr[jolt - 2], 
            jolt_cntr[jolt - 3]])
        print(f'Adding {jolt_cntr[jolt - 1]} {jolt-1}s + {jolt_cntr[jolt - 2]} {jolt-2}s + {jolt_cntr[jolt - 3]} {jolt-3}s')
        print(f'New jolt_cntr is {jolt_cntr}')
    return jolt_cntr[max_jolts]


if __name__ == "__main__":
    
    with open('day10.txt') as fin:
        contents = sorted([int(line.strip()) for line in fin.readlines()])

    value = count_the_shit(contents)
    print(value)


