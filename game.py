from game_constants import *


class Game:
    def __init__(self, display=pygame.display.set_mode((W * BLOCK_SIZE, H * BLOCK_SIZE))):
        self.display = display
        pygame.display.set_caption('Reverse Pacman')

        self.clock = pygame.time.Clock()

        self.pac = PAC
        self.pac_dir = STAY

        self.blinky = BLINKY
        self.blinky_dir = STAY

        self.pinky = PINKY
        self.pinky_dir = STAY

        self.inky = INKY
        self.inky_dir = STAY

        self.clyde = CLYDE
        self.clyde_dir = STAY

        self.score = 0

    def step(self, a_pac, a1, a2, a3, a4):
        # TODO: add teleportation to the the game using modulus when calculating new position

        # Move pacman
        pac_p = ((self.pac[0] + a_pac[0]) % W, (self.pac[1] + a_pac[1]) % H)
        if a_pac in COMPASS_ROSE and valid_point(pac_p):
            self.pac_dir = a_pac
        pac_p = ((self.pac[0] + self.pac_dir[0]) % W, (self.pac[1] + self.pac_dir[1]) % H)
        if valid_point(pac_p):
            self.pac = pac_p
        moved_into_occupied_space = self.is_over()

        # Move ghost1
        if a1 in COMPASS_ROSE:
            self.blinky_dir = a1
        else:
            self.blinky_dir = STAY
        blinky_p = ((self.blinky[0] + self.blinky_dir[0]) % W, (self.blinky[1] + self.blinky_dir[1]) % H)
        if valid_point(blinky_p):
            self.blinky = blinky_p

        # Move ghost 2
        if a2 in COMPASS_ROSE:
            self.pinky_dir = a2
        else:
            self.pinky_dir = STAY
        pinky_p = ((self.pinky[0] + self.pinky_dir[0]) % W, (self.pinky[1] + self.pinky_dir[1]) % H)
        if valid_point(pinky_p):
            self.pinky = pinky_p

        # Move ghost3
        if a3 in COMPASS_ROSE:
            self.inky_dir = a3
        else:
            self.inky_dir = STAY
        inky_p = ((self.inky[0] + self.inky_dir[0]) % W, (self.inky[1] + self.inky_dir[1]) % H)
        if valid_point(inky_p):
            self.inky = inky_p

        # Move ghost4
        if a4 in COMPASS_ROSE:
            self.clyde_dir = a4
        else:
            self.clyde_dir = STAY
        clyde_p = ((self.clyde[0] + self.clyde_dir[0]) % W, (self.clyde[1] + self.clyde_dir[1]) % H)
        if valid_point(clyde_p):
            self.clyde = clyde_p

        self.score += 1
        self.clock.tick(FPS)

        return self.is_over() if self.is_over() else moved_into_occupied_space

    def draw(self):

        self.display.fill(BLACK)
        for y in range(H):
            for x in range(W):
                if not valid_point((x, y)):
                    pygame.draw.rect(self.display, WALL_COLOR,
                                     pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                if (x, y) == self.pac:
                    pygame.draw.rect(self.display, PAC_COLOR,
                                     pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                if (x, y) == self.blinky:
                    pygame.draw.rect(self.display, BLINKY_COLOR,
                                     pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                if (x, y) == self.pinky:
                    pygame.draw.rect(self.display, PINKY_COLOR,
                                     pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                if (x, y) == self.inky:
                    pygame.draw.rect(self.display, INKY_COLOR,
                                     pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                if (x, y) == self.clyde:
                    pygame.draw.rect(self.display, CLYDE_COLOR,
                                     pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

            pygame.display.flip()

    def get_state(self):
        return [{'loc': self.pac, 'last': self.pac_dir}, {'loc': self.blinky, 'last': self.blinky_dir},
                {'loc': self.pinky, 'last': self.pinky_dir}, {'loc': self.inky, 'last': self.inky_dir},
                {'loc': self.clyde, 'last': self.clyde_dir}]

    def is_over(self):
        game_over = None
        if self.pac == self.blinky:
            game_over = 1

        if self.pac == self.pinky:
            game_over = 2

        if self.pac == self.inky:
            game_over = 3

        if self.pac == self.clyde:
            game_over = 4

        return game_over
