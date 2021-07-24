from game_constants import *
from abc import ABC
from collections import deque
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
            d = dist(p, target)
            if d < min_dist:
                min_dist = d
                min_idx = points.index(p)

        return dirs[min_idx]


class Complicated(Ghost):
    def __init__(self, location, depth):
        self.location = location
        self.last_dir = STAY
        self.depth = depth

    def action(self, state):
        pac, blinky, pink, inky, clyde = state
        dirs = [UP, LEFT, DOWN, RIGHT]  # all directions possible
        points = [((self.location[0] + d[0]) % W, (self.location[1] + d[1]) % H) for d in dirs]  # all points around ghost
        head = PosTreeNode(pac, self.depth)
        comp_tree(head, 00000, pac, self.depth) # 00000 should be the last move pacman made which is the same as his diraction
        score = {}
        for point in points:
            score[point] = 0
            comp_queue = deque()
            comp_queue.append(head)
            while comp_queue:
                comp_curr = comp_queue.pop()
                target = comp_curr.location
                achiveable = False
                if not abs(target[0] - point[0]) + abs(target[1] - point[1]) > self.depth - comp_curr.depth:
                    bfs_head = PosTreeNode(point, self.depth - comp_curr.depth)
                    bfs_tree(bfs_head, dirs[points.index(point)], point, self.depth - comp_curr.depth)
                    bfs_queue = deque()
                    bfs_queue.append(bfs_head)
                    while bfs_queue:
                        bfs_curr = bfs_queue.pop()
                        if (bfs_curr.location == target):
                            achiveable = True
                            break
                if achiveable:
                    score[point] += comp_curr.rec_size()
                else:
                    for node in comp_curr.nodes:
                        comp_queue.append(node)
        max = 0
        max_point = STAY
        for point in points:
            if score[point] > max:
                max = score[point]
                max_point = point
        if max == 0:
            min = 1000
            for point in points:
                if dist(point, pac) < min:
                    min = score[point]
                    max_point = point
        return dirs[points.index(max_point)]







def dist(point1, point2):
    return math.sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))


def comp_tree(node, last, loc, depth):
    if depth == 0:
        return
    dirs = [UP, LEFT, DOWN, RIGHT]  # all directions possible
    for dir in dirs:
        if dir == list(map(lambda x: -x, last)):
            dirs.remove(dirs.index(dir))
    points = [((loc[0] + d[0]) % W, (loc[1] + d[1]) % H) for d in dirs]
    for p in points:
        if not valid_point(p):  # if point not valid remove it
            idx = points.index(p)
            points.remove(p)
            dirs.remove(dirs[idx])
    if len(points) > 1:
        new_node = PosTreeNode(loc, depth)
        node.add_node(new_node)
    else:
        new_node = node

    for idx in range(len(points)):
        comp_tree(new_node, dirs[idx], points[idx], depth-1)


def bfs_tree(node, last, loc, depth):
    if depth == 0:
        return
    dirs = [UP, LEFT, DOWN, RIGHT]  # all directions possible
    for dir in dirs:
        if dir == list(map(lambda x: -x, last)):
            dirs.remove(dirs.index(dir))
    points = [((loc[0] + d[0]) % W, (loc[1] + d[1]) % H) for d in dirs]
    for p in points:
        if not valid_point(p):  # if point not valid remove it
            idx = points.index(p)
            points.remove(p)
            dirs.remove(dirs[idx])
    new_node = PosTreeNode(loc, depth)
    node.add_node(new_node)
    for idx in range(len(points)):
        comp_tree(new_node, dirs[idx], points[idx], depth-1)

class PosTreeNode:
    def __init__(self, location, depth):
        self.location = location
        self.nodes = []
        self.depth = depth

    def add_node(self, node):
        self.nodes.append(node)

    def rec_size(self):
        if self.nodes:
            sum = 1
            for node in self.nodes:
                sum += node.rec_size
            return sum
        return 1
