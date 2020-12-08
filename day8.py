from copy import deepcopy


def process_node(local_instructions, head, a, flag):
    print(f'Head: {head}, A: {a}')
    i = local_instructions[head]
    local_instructions[head] = 'X'
    print(f'  Instruction is {i}')
    if i[0] == 'nop':
        head += 1
    elif i[0] == 'acc':
        a += int(i[1])
        head += 1
    elif i[0] == 'jmp':
        head += int(i[1])
    elif i[0] == 'X':
        flag = False
        print(f'Repeating an instruction and a is {a}')

    
    return local_instructions, head, a, flag


def process_list(nopsnjumps, base_instructions):
    for nj in nopsnjumps:
        # reset all the variables
        flag = True
        instructions = deepcopy(base_instructions)
        a = 0
        head = 0

        # change the next nop/jump
        if instructions[nj][0] == 'nop':
            instructions[nj][0] = 'jmp'
        elif instructions[nj][0] == 'jmp':
            instructions[nj][0] = 'nop'
        else:
            raise "CONFUSED ON INSTRUCTIONS"
        
        # run part 1
        while flag:
            instructions, head, a, flag = process_node(instructions, head, a, flag)
            if head >= len(instructions):
                return a


if __name__ == "__main__":
    with open('day8.txt') as fin:
        base_instructions = [line.strip().split() for line in fin.readlines()]

    nopsnjumps = [i for i, x in enumerate(base_instructions) if x[0] in ['nop', 'jmp']]

    a = process_list(nopsnjumps, base_instructions)
    print(f'Complete, accumulated value is {a}')