from game_constants import *
from abc import ABC
import random
import math


class Ghost(ABC):
    def __init__(self, location):
        self.location = location

    def action(self, state):
        return STAY


class Random(Ghost):

    def action(self, state):
        return random.choice(COMPASS_ROSE)


class PacRepeat(Ghost):
    # FIXME: for some reason not working
    def __init__(self, location):
        self.last = STAY

    def action(self, state):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # checking if the current event is a key pressing
                if event.key == pygame.K_a:  # left arrow -> return LEFT direction
                    print('L')
                    self.last = LEFT
                    return LEFT
                elif event.key == pygame.K_d:  # right arrow -> return RIGHT direction
                    print('R')
                    self.last = RIGHT
                    return RIGHT
                elif event.key == pygame.K_w:  # up arrow -> return UP direction
                    print('U')
                    self.last = UP
                    return UP
                elif event.key == pygame.K_s:  # down arrow -> return DOWN direction
                    print('D')
                    self.last = DOWN
                    return DOWN

        return self.last  # if no arrow was detected return the stay direction


class Blinky(Ghost):
    def __init__(self, location):
        super(Blinky, self).__init__(location)
        self.last_dir = STAY

    def action(self, state):
        pac, blinky, pink, inky, clyde = state
        target = pac
        dirs = [UP, LEFT, DOWN, RIGHT]  # all directions possible
        points = [((self.location[0] + d[0]) % W, (self.location[1] + d[1]) % H) for d in dirs]  # all points around ghost

        # If last directions is not stay - that means the last directions has a back to it
        if self.last_dir != STAY:
            for dir in dirs:  # looping through all the directoins
                idx = COMPASS_ROSE.index(self.last_dir)
                dir_idx = COMPASS_ROSE.index(dir)
                if abs(idx - dir_idx) == 2:  # It the current directions is back to the last directions remove it
                    dirs.remove(dir)
                    points.remove(points[dir_idx])

        # looping through all the points
        for p in points:
            if not valid_point(p):  # if point not valid remove it
                idx = points.index(p)
                points.remove(p)
                dirs.remove(dirs[idx])

        if len(points) == 0:  # if no point left return STAY
            print('No point found')
            return self.last_dir

        min_dist = 1_000_000
        min_idx = 5

        for p in points:
            d = math.dist(p, target)
            if d < min_dist:
                min_dist = d
                min_idx = points.index(p)

        print(dirs[min_idx])
        return dirs[min_idx]

