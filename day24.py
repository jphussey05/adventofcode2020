from collections import Counter
from copy import deepcopy


class Tile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.adjacencies = self._adjacent_points()
 

    def _adjacent_points(self):
        offsets = [
            (2,0),
            (-2,0),
            (1,1),
            (-1,-1),
            (-1,1),
            (1,-1)
        ]

        return [(self.x + x, self.y + y) for x, y in offsets]


def get_dir(chars):
    cur = ''
    for c in chars:
        cur += c
        if cur in ['e', 'w', 'se', 'sw', 'ne', 'nw']:
            return cur, chars[len(cur):]
        

if __name__ == "__main__":
    
    with open('day24.txt') as fin:
        contents = [line.strip() for line in fin.readlines()]
    
    tiles = dict()

    move_dict = {
        'e': (2,0),
        'w': (-2,0),
        'se': (1,1),
        'sw': (-1,1),
        'ne': (1,-1),
        'nw': (-1,-1)
    }
    for line in contents:
        x, y = 0, 0  # all lines start from reference in center
        
        while line:
            #get a direction
            direction, line = get_dir(line)
            # move that direction
            x += move_dict[direction][0]
            y += move_dict[direction][1]
        
        #when at end, 'activate' the tile
        if (x,y) in tiles:
            del tiles[(x,y)]
        else:
            tiles[(x,y)] = Tile(x, y)
    
    print(f'Total black tiles is {len(tiles)}')


    for day in range(1,101):

        adj_cnt = Counter()
        next_tiles = dict()

        for coord, tile in tiles.items():           # look at all active points
            active_neighbors = 0
            for neighbor in tile.adjacencies:       # look at each neighbor
                if neighbor not in tiles:           # neighbor is a white tile
                    adj_cnt[neighbor] += 1
                else:                               # neighbor is a black tile
                    active_neighbors += 1

            if active_neighbors in [1,2]:           #stays active 
                next_tiles[coord] = tile
        
        for inactive in adj_cnt:                    # whites next to blacks
            if adj_cnt[inactive] == 2:
                next_tiles[inactive] = Tile(inactive[0], inactive[1])
        
        tiles = deepcopy(next_tiles)
        
        
    print(f'*DAY {day}: {len(tiles)}')
        