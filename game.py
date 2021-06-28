from game_constants import *


class Game:
    def __init__(self, display=pygame.display.set_mode((W * BLOCK_SIZE, H * BLOCK_SIZE))):
        self.display = display
        pygame.display.set_caption('Reverse Pacman')

        self.clock = pygame.time.Clock()

        self.pac = PAC
        self.pac_dir = STAY

        self.g1 = G1
        self.g2 = G2
        self.g3 = G3
        self.g4 = G4

        self.turn = 0

    def step(self):
        pass

