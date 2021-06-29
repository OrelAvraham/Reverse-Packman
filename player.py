from game_constants import *


class Player:

    def __init__(self):
        self.last = STAY

    def action(self):

        # looping over the game events to check for keyboard input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # checking if the current event is a key pressing
                if event.key == pygame.K_LEFT:  # left arrow -> return LEFT direction
                    self.last = LEFT
                    return LEFT
                elif event.key == pygame.K_RIGHT:  # right arrow -> return RIGHT direction
                    self.last = RIGHT
                    return RIGHT
                elif event.key == pygame.K_UP:  # up arrow -> return UP direction
                    self.last = UP
                    return UP
                elif event.key == pygame.K_DOWN:  # down arrow -> return DOWN direction
                    self.last = DOWN
                    return DOWN

        return self.last  # if no arrow was detected return the stay direction

