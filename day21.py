
from collections import Counter, defaultdict
from pprint import pprint
from copy import deepcopy

def check_lengths(allergen_map):
    # rip through dictionary, first value that still has more than one item 
    # fails the test, need to further reduce
    for v in allergen_map.values():
        if len(v) != 0:
            return False
    
    return True


def reduce_map(allergen_map):
    # do somethings to find the next item with a 1:1
    # look for the first item in dict that has length 1
    # loop through all items again, if you don't find it, continue to next
    # otherwise, remove it from everything and return new reduced map with the final map
    reduced_map = deepcopy(allergen_map)
    print(reduced_map)
    for k, v in allergen_map.items():
        if len(allergen_map.keys()) == 1:
            print(f'Last item!')
            # last item
            del reduced_map[k]
            return k, list(v)[0], reduced_map
        elif len(v) == 1:
            
            v = list(v)[0]
            print(f'{k} only has {v}')
            for k2, v2 in allergen_map.items():
                if k == k2:
                    continue
                elif v in v2:
                    reduced_map[k2].remove(v)
                    # print(reduced_map[k])
                    del reduced_map[k]
    
            return k, v, reduced_map

    return None, reduced_map

if __name__ == "__main__":
    with open('day21.txt') as fin:
        contents = [line.strip() for line in fin.readlines()]

    count = Counter()
    allergen_dict = defaultdict(list)
    for line in contents:
        ingredients, allergens = line.split(' (')
        ingredients = set(ingredients.split())
        for i in ingredients:
            count[i] += 1

        allergens = set(allergens[9:-1].split(', '))
        for a in allergens:
            allergen_dict[a].append(ingredients)

    # pprint(allergen_dict)

    allergen_only_dict = defaultdict(list)
    possible_ingredients = []
    for allergen, ingredient_sets in allergen_dict.items():
        if len(ingredient_sets) == 1:
            # print(f'{allergen} could be {ingredient_sets[0]}')
            possible_ingredients.extend(ingredient_sets[0])
            allergen_only_dict[allergen] = ingredient_sets[0]
        else:
            tmp = ingredient_sets[0]
            for i_set in ingredient_sets[1:]:
                tmp = tmp.intersection(i_set)
            
            
            # print(f'{allergen} could be {tmp}')
            possible_ingredients.extend(tmp)
            allergen_only_dict[allergen] = tmp
    
    # pprint(allergen_only_dict)
    non_allergens = set(count.keys()).difference(set(possible_ingredients))
    print(f'The total appearance of non-dangeours ingredients is: {sum([count[na] for na in non_allergens])}')
    print(f'These ingredients are not dangerous: {", ".join(non_allergens)}')

    final_map = dict()
    while not check_lengths(allergen_only_dict):
        print(f'Still not right')
        print(allergen_only_dict)
        final_map_k, final_map_v, allergen_only_dict = reduce_map(allergen_only_dict)
        
        if final_map_k:
            final_map[final_map_k] = final_map_v

        

    print(final_map)

    


    output = [final_map[k] for k in sorted(final_map)]
    print(','.join(output))