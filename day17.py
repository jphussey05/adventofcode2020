from math import sqrt
from itertools import product
from copy import deepcopy
from collections import Counter
from time import time

class Point(object):
    def __init__(self, x, y, z, w,state='inactive'):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.state = state
        self.adjacencies = self._adjacent_points()
 

    def _adjacent_points(self):
        offsets = product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1])
        neighbors = [(self.x + x, self.y + y, self.z + z, self.w + w) for x, y, z, w in offsets]
        neighbors.remove((self.x, self.y, self.z, self.w))
        return set(neighbors)

    def __str__(self):
        return f'Point {self.x},{self.y},{self.z},{self.w}: {self.state}'

    def __repr__(self):
        return f'Point({self.x}, {self.y}, {self.z}, {self.w}, {self.state})'


# def count_active_neighbors(point, actives, database):
#     cnt = 0
#     points_to_add = []
#     for adj in point.adjacencies:
#         if adj in actives:   # it's in the db and active
#             cnt += 1
#         elif adj not in database:    # it's not in db, add it
#             points_to_add.append(Point(adj[0], adj[1], adj[2], adj[3], state='inactive'))
    
#     return cnt, points_to_add


if __name__ == "__main__":
    with open('day17.txt') as fin:
        contents = [line.strip() for line in fin.readlines()]
    t0 = time()
    # initial population of database with active Points
    database = {}
    for y, row in enumerate(contents):
        for x, point in enumerate(row):
            if point == '#':
                database[(x, -y, 0, 0)] = Point(x, -y, 0, 0, 'active')

    print(f'Initial number of actives is {len(database)}')
    deltas = 0
    t1 = time()
    for n in range(6):
        t2 = time()
        adj_cntr = Counter()
        next_db = {}
        for key, point in database.items():         # look at all active points
            active_neighbors = 0
            for neighbor in point.adjacencies:      # look at each neighbor 
                if neighbor not in database.keys(): # if neighbor isn't active, add to cntr
                    adj_cntr[neighbor] += 1
                else:                               # neighbor was active
                    active_neighbors += 1
            
            if active_neighbors in [2,3]:           # the 'stay active' check
                next_db[key] = point
        
        for inactive in adj_cntr:                   # the 'activate an inactive' check
            if adj_cntr[inactive] == 3:
                next_db[inactive] = Point(inactive[0], inactive[1], inactive[2], inactive[3], state='active')

        # print(f'Number active after {n+1} rounds is {len(next_db)}')
        database = deepcopy(next_db)
        t3 = time()
        deltas += (t3-t2)
    t4 = time()
    print(f'Time to populate initial = {t1 - t0}')
    print(f'Average loop time = {deltas / 6}')
    print(f'Total time = {t4-t0}')