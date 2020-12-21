from copy import deepcopy
from pprint import pprint

def remove_element(ele, template):
    for t in template:
        if ele in t:
            t.remove(ele)

    return template


def template_check(template):
    for t in template:
        if len(t) > 1:
            return False    
    return True


def your_tix_multiply(correct_perm, your_tix):
    answer = 1
    return answer


def validate_tix(ticket, valid_nums, all_valids):
    for val in ticket:
        if val in all_valids:
            continue
        else:
            return False

    return True


if __name__ == "__main__":
    with open('day16.txt') as fin:
        contents = [line.strip() for line in fin.readlines()]
    
    valid_nums = {}
    valid_tix = set()

    for idx, line in enumerate(contents):
        
        if not line:  # skip blank lines
            continue
        if 'your ticket' in line:  # stop at your ticket for now
            idx += 1
            break        
        colon_sep = line.split(':')
        range1, range2 = colon_sep[1].split(' or ')

        range1 = list(map(int, range1.split('-')))
        range2 = list(map(int, range2.split('-')))
        range1_nums = list(range(range1[0], range1[1] + 1))
        range2_nums = list(range(range2[0], range2[1] + 1))

        valid_nums[colon_sep[0]] = range1_nums + range2_nums
    
    all_valids = []
    for v in valid_nums.values():
        all_valids.extend(v)
    all_valids = set(all_valids)

    your_tix = list(map(int, contents[idx].split(',')))

    template = [list(valid_nums.keys()) for _ in range(len(valid_nums.keys()))]
    nearby_tix = [list(map(int, line.split(','))) for line in contents[idx+3:]]


    valid_tix = [t for t in nearby_tix if validate_tix(t, valid_nums, all_valids)]
                
    for t in valid_tix:
            # print(f'Looking at {t}')
            for idx, value in enumerate(t):
                bad_keys = []
                tmp_keys = deepcopy(template[idx])
                for key in tmp_keys:
                    
                    # print(f' Checking {value} in {key}')
                    if value in valid_nums[key]:
                        continue
                    else:
                        # print(f'{value} is not in {key}')
                        bad_keys.append(key)

                for bk in bad_keys:
                    # print(f'Removing {bk} from {template[idx]}')
                    template[idx].remove(bk)

  
    pprint(template)

    answer = 1
    departures = [0, 8, 10, 11, 17, 19]
    for d in departures:
        answer *= your_tix[d]

    print(answer)