
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


def part2(contents):
    buses = [(bus, i) for i, bus in enumerate(contents[1].split(','))]
    print(buses)
    

if __name__ == "__main__":
    
    with open('day13.txt') as fin:
        contents = [line.strip() for line in fin.readlines()]

    # part1(contents)
    part2(contents)