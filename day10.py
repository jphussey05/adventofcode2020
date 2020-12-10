



with open('day10.txt') as fin:
    contents = sorted([int(line.strip()) for line in fin.readlines()])

current_jolts = 0

print(contents)

ones = 0
threes = 0

while len(contents) > 0:
    adapter = contents.pop(0)
    print(f'The next adapter is {adapter}, jolts are {current_jolts}')
    if adapter <= current_jolts + 3:
        print(f'  Adapter checks out')
        if adapter == current_jolts + 1:
            print(f'  That is a diff of 1')
            ones += 1
        elif adapter == current_jolts + 3:
            print(f'  That is a diff of 3')
            threes += 1
        current_jolts = adapter
    else:
        #bail?
        print('Next item was not within 3')
        break

print(ones * (threes + 1))