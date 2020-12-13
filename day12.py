class Ship(object):
    def __init__(self):
        self.degree = 90
        self.pos = (0,0)
        self.deg_dict = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
        self.waypoint = (10, 1)
        return

    def move_forward(self, dist):
        self.pos = self.pos[0] + dist * self.waypoint[0], self.pos[1] + dist * self.waypoint[1]
        return

    def move_east(self, dist):
        self.waypoint = self.waypoint[0] + dist, self.waypoint[1]
        return

    def move_west(self, dist):
        self.waypoint = self.waypoint[0] - dist, self.waypoint[1]
        return

    def move_north(self, dist):
        self.waypoint = self.waypoint[0], self.waypoint[1] + dist
        return

    def move_south(self, dist):
        self.waypoint = self.waypoint[0], self.waypoint[1] - dist
        return

    def turn(self, turn_dir, deg):
        while deg > 0:
            deg -= 90

            if turn_dir == 'R':
                self.waypoint = self.waypoint[1], self.waypoint[0] * -1
            elif turn_dir == 'L':
                self.waypoint = self.waypoint[1] * -1, self.waypoint[0]
            else:
                raise NotImplementedError

        return

    def manhattan(self):
        return abs(self.pos[0]) + abs(self.pos[1])

    def __str__(self):
        return f'{self.pos} at a distance of {self.manhattan()} from origin, the waypoint is {self.waypoint}'


if __name__ == "__main__":
    with open('day12.txt') as fin:
        contents  = [line.strip() for line in fin.readlines()]
    
    ship = Ship()
    
    for move in contents:

        instruction = move[0]
        unit = int(move[1:])
        print(move)

        if instruction == 'F':
            ship.move_forward(unit)
        elif instruction in ['L', 'R']:
            ship.turn(instruction, unit)
        elif instruction == 'E':
            ship.move_east(unit)
        elif instruction == 'W':
            ship.move_west(unit)
        elif instruction == 'N':
            ship.move_north(unit)
        elif instruction == 'S':
            ship.move_south(unit)
        else:
            raise "NOT SURE WHAT THIS INSTRUCTION IS"

        print(ship)
    print(ship.manhattan())   