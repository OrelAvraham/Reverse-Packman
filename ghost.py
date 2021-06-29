from game_constants import *
from abc import ABC
import random


class Ghost(ABC):

    def action(self, state):
        return STAY


class blinky(Ghost):

    def action(self, state):
        return random.choice(COMPASS_ROSE)


class pinky(Ghost):

    def __init__(self):
        self.last = STAY

    def action(self, state):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # checking if the current event is a key pressing
                if event.key == pygame.K_a:  # left arrow -> return LEFT direction
                    self.last = LEFT
                    return LEFT
                elif event.key == pygame.K_d:  # right arrow -> return RIGHT direction
                    self.last = RIGHT
                    return RIGHT
                elif event.key == pygame.K_w:  # up arrow -> return UP direction
                    self.last = UP
                    return UP
                elif event.key == pygame.K_s:  # down arrow -> return DOWN direction
                    self.last = DOWN
                    return DOWN

        return self.last  # if no arrow was detected return the stay direction


