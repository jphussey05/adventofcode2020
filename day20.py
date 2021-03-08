from collections import defaultdict
from numpy import transpose, flip
from pprint import pprint
from copy import deepcopy

class Tile(object):
    def __init__(self, id):
        self.layout = list()
        self.id = id
        self.neighbors = defaultdict(set)
        self.flipped = False
        self.rotation = 0

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.layout])

    def rot90(self):
        self.layout = list(map(list, map(reversed, transpose(self.layout))))
        self.rotation = (self.rotation + 90) % 360

    def flip(self):
        self.layout = list(map(list, flip(self.layout, axis=1)))
        self.flipped = not self.flipped

    def left_edge(self):
        return [row[0] for row in self.layout]

    def right_edge(self):
        return [row[-1] for row in self.layout]

    def top_edge(self):
        return self.layout[0]

    def bot_edge(self):
        return self.layout[-1]


def compare_tiles(a: Tile, b: Tile):
    # populate a's neighbors with b orientations
    for _ in range(4):        
        if a.left_edge() == b.right_edge():
            a.neighbors['L'].add(b.id)
        if a.right_edge() == b.left_edge():
            a.neighbors['R'].add(b.id)
        if a.top_edge() == b.bot_edge():
            a.neighbors['U'].add(b.id)
        if a.bot_edge() == b.top_edge():
            a.neighbors['D'].add(b.id)
        
        b.rot90()

    b.flip()

    for _ in range(4):
        #check it
        if a.left_edge() == b.right_edge():
            a.neighbors['L'].add(b.id)
        if a.right_edge() == b.left_edge():
            a.neighbors['R'].add(b.id)
        if a.top_edge() == b.bot_edge():
            a.neighbors['U'].add(b.id)       
        if a.bot_edge() == b.top_edge():
            a.neighbors['D'].add(b.id)
    
    b.flip()


def parse_tiles(contents):
    tile_dict = dict()
    for line in contents:
        if 'Tile' in line:
            key = line[5:9]
            tile_dict[key] = Tile(key)
            continue
        elif not line:
            continue
        else:
            tile_dict[key].layout.append(line)

    return tile_dict


if __name__ == "__main__":
    with open('day20.txt') as fin:
        contents = [line.strip() for line in fin.readlines()]

    tile_dict = parse_tiles(contents)

    

    for k1, v1 in tile_dict.items():
        # print(f'Key {k1} has {len(v1.layout)} values')
        for k2, v2 in tile_dict.items():
            if k1 == k2:
                continue
            else:
                # have to do the flips for the "a" tile here
                compare_tiles(v1, v2)
        print(f'Key {k1} has neighbors = {v1.neighbors})')
            
    # b = Tile('b', [['*','o'],['o','o']])
    # a = Tile('a', [['o','*'],['o','o']])


    # print(f'B neighbors = {b.neighbors}')
    # compare_tiles(b, a)
    # print(f'B neighbors = {b.neighbors}')
  
    # the question is: which tile, in any orientation, has no bordering corners