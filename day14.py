from itertools import product
from copy import deepcopy

def get_mask(mask):
    mask_dict = {}
    while mask.count('1') > 0:
        idx = mask.index('1')
        mask_dict[idx] = 1
        mask[idx] = '0'
    
    while mask.count('X') > 0:
        idx = mask.index('X')
        mask_dict[idx] = 'X'
        mask[idx] = '0'

    return mask_dict


def overwrite(addr, mask):
    x_bit_cnt = 0
    new_addrs = []
    floating_idxs = []
    for position, bit in mask.items():
        if bit == 1:
            addr[position] = str(bit)
        elif bit == 'X':
            x_bit_cnt += 1
            floating_idxs.append(position)

    x_bit_list = [[0,1] for _ in range(x_bit_cnt)]
    x_bit_product = list(product(*x_bit_list))
    for x_bits in x_bit_product:
        temp_addr = deepcopy(addr)
        for idx, fi in enumerate(floating_idxs):
            temp_addr[fi] = str(x_bits[idx])
        
        new_addrs.append(temp_addr)
        
    return new_addrs


if __name__ == "__main__":
    
    with open('day14.txt') as fin:
        contents = [line.strip() for line in fin.readlines()]

    mem = dict()

    for line in contents:
        inst, val = line.split(' = ')
        if inst == 'mask':
            mask = get_mask(list(val))
        elif 'mem' == inst[:3]:
            addr = inst[4:-1]
            addr = format(int(addr), '036b')
            result = overwrite(list(addr), mask)
            
            for a in result:
                a = ''.join(a)
                mem[int(a, base=2)] = int(val)

    print(sum([v for v in mem.values()]))
            
