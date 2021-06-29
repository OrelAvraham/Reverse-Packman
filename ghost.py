from game_constants import *
from abc import ABC


class Ghost(ABC):

    def action(self, state):
        return STAY
