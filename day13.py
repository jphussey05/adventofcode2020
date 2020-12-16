from datetime import datetime
import math

def find_next_arrival(arrival_time, bus):
    bus_time = bus  # assuming we won't arrive from 0 -> first loop
    while bus_time < arrival_time:
        bus_time += bus
    return bus_time - arrival_time

def part1(contents):
    arrival_time = int(contents[0])
    buses = [int(bus) for bus in contents[1].split(',') if bus != 'x']

    wait_time = 1000000
    for bus in buses:
        bus_wait_time = find_next_arrival(arrival_time, bus)
        if bus_wait_time < wait_time:
            wait_time = bus_wait_time
            best_bus = bus

    print(f'The minimum wait time is {wait_time} minutes for bus {best_bus}')
    print(f'Part 1 answer is {wait_time * best_bus}')


def inverse(Ni, ni):
    print(f'Invers with:\n{Ni}\n{ni}')
    multiple = Ni % ni
    remainder = -1
    x = 1
    while remainder == -1:
        if x * multiple % ni == 1:
            print(x * multiple % ni)
            print(f'Returning {x}')
            return x
        else:
            x += 1

def part2(contents):
    buses = [bus for bus in contents[1].split(',')]
    for i, bus in enumerate(buses):
        if bus != 'x':
            print(i, bus)
    bs = [(int(b) - i) % int(b) for i, b in enumerate(buses) if (b != 'x')]
    ns = [int(b) for i, b in enumerate(buses) if (b != 'x')]

    for n in ns:
        N = N * n
    print(N)
    NS = [N / n for n in ns]
    xs = [inverse(Ni, ni) for Ni, ni in zip(NS, ns)]
    bNx = list(zip(bs, NS, xs))

    items = [combo[0] * combo[1] * combo[2] for combo in bNx]
    
    print(f'Remainders {bs}')
    print(NS)
    print(xs)
    print(bNx)
    print(items)
    print(sum(items) % N)

    
if __name__ == "__main__":
    
    with open('day13.txt') as fin:
        contents = [line.strip() for line in fin.readlines()]

    # part1(contents)
    part2(contents)
    