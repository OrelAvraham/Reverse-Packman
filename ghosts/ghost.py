from game_constants import *
from abc import ABC
from collections import deque
import random
import math


class Ghost(ABC):
    def __init__(self, location, name=None):
        self.location = location
        self.name = name

    def action(self, state, self_idx):
        return STAY

    def __str__(self):
        return 'Generic Ghost'


class Random(Ghost):

    def action(self, state, self_idx):
        return random.choice(COMPASS_ROSE)

    def __str__(self):
        return self.name


def dist(point1, point2):
    return math.sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))