from ghost import *
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
