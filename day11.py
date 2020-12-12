from copy import deepcopy

def print_map(layout):
    for line in layout:
        print(''.join(line))
    print('--------------------')

def count_seats(layout):
    return sum([row.count('#') for row in layout])

def count_adjacencies(ridx, sidx, layout):
    moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    adj = 0
    max_rows = len(layout) - 1
    max_seats = len(layout[0]) - 1 

    for y, x in moves:
        new_row = ridx + y
        new_seat = sidx + x
        while not (new_row < 0 or new_seat < 0 or new_row > max_rows or new_seat > max_seats):
            
            sees = layout[new_row][new_seat]
            if sees == '#':
                adj += 1
                break
            elif sees == 'L':
                break
            else:
                new_row = new_row + y
                new_seat = new_seat + x
            
        
        
    return adj


def update_seats(layout):
    moves = 0
    new_layout = deepcopy(layout)
    for ridx, row in enumerate(layout):
        for sidx, seat in enumerate(row):
            if seat == '.':
                continue

            adj = count_adjacencies(ridx, sidx, layout)

            if seat == 'L' and adj == 0:
                new_layout[ridx][sidx] = '#'
                moves += 1
            elif seat == '#' and adj >= 5:
                new_layout[ridx][sidx] = 'L'
                moves +=1
            else:
                continue

    return moves, new_layout

if __name__ == "__main__":
    with open('day11.txt') as fin:
        contents = [list(line.strip()) for line in fin.readlines()]

    print_map(contents)
    num_moves, layout = update_seats(contents)
    print(f'{num_moves} moves, {count_seats(layout)} seats filled.')
    print_map(layout)
        
    while num_moves > 0:
        num_moves, layout = update_seats(layout)
        print(f'{num_moves} moves, {count_seats(layout)} seats filled.')
        
