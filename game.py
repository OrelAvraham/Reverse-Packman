from game_constants import *


class Game:
    def __init__(self, display=pygame.display.set_mode((W * BLOCK_SIZE, H * BLOCK_SIZE))):
        self.display = display
        pygame.display.set_caption('Reverse Pacman')

        self.clock = pygame.time.Clock()

        self.pac = PAC
        self.pac_dir = STAY

        self.g1 = G1
        self.g1_dir = STAY

        self.g2 = G2
        self.g2_dir = STAY

        self.g3 = G3
        self.g3_dir = STAY

        self.g4 = G4
        self.g4_dir = STAY

        self.turn = 0

    def step(self, a_pac, a1, a2, a3, a4):
        # TODO: add teleportation to the the game using modulus when calculating new position

        # Move pacman
        if a_pac in COMPASS_ROSE:
            self.pac_dir = a_pac
        pac_p = tuple([a + b for a, b in zip(self.pac, self.pac_dir)])
        if valid_point(pac_p):
            self.pac = pac_p

        # Move ghost1
        if a1 in COMPASS_ROSE:
            self.g1_dir = a1
        else:
            self.g1_dir = STAY
        g1_p = tuple([a + b for a, b in zip(self.g1, self.pac_dir)])
        if valid_point(g1_p):
            self.g1 = g1_p

        # Move ghost 2
        if a2 in COMPASS_ROSE:
            self.g2_dir = a1
        else:
            self.g2_dir = STAY
        g2_p = tuple(a + b for a, b in zip(self.g2, self.pac_dir))
        if valid_point(g2_p):
            self.g2 = g2_p

        # Move ghost3
        if a3 in COMPASS_ROSE:
            self.g3_dir = a1
        else:
            self.g3_dir = STAY
        g3_p = tuple(a + b for a, b in zip(self.g3, self.pac_dir))
        if valid_point(g3_p):
            self.g3 = g3_p

        # Move ghost4
        if a4 in COMPASS_ROSE:
            self.g4_dir = a1
        else:
            self.g4_dir = STAY
        g4_p = tuple(a + b for a, b in zip(self.g4, self.pac_dir))
        if valid_point(g4_p):
            self.g4 = g4_p

        self.clock.tick(FPS)

    def draw(self):
        self.display.fill(BLACK)
        for y in range(H):
            for x in range(W):
                if not valid_point((x, y)):
                    pygame.draw.rect(self.display, WALL_COLOR,
                                     pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, (x + 1) * BLOCK_SIZE,
                                                 (y + 1) * BLOCK_SIZE))
                if (x, y) == self.pac:
                    pygame.draw.rect(self.display, PAC_COLOR,
                                     pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, (x + 1) * BLOCK_SIZE,
                                                 (y + 1) * BLOCK_SIZE))
                if (x, y) == self.g1:
                    pygame.draw.rect(self.display, G1_COLOR,
                                     pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, (x + 1) * BLOCK_SIZE,
                                                 (y + 1) * BLOCK_SIZE))
                if (x, y) == self.g2:
                    pygame.draw.rect(self.display, G2_COLOR,
                                     pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, (x + 1) * BLOCK_SIZE,
                                                 (y + 1) * BLOCK_SIZE))
                if (x, y) == self.g3:
                    pygame.draw.rect(self.display, G3_COLOR,
                                     pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, (x + 1) * BLOCK_SIZE,
                                                 (y + 1) * BLOCK_SIZE))
                if (x, y) == self.g4:
                    pygame.draw.rect(self.display, G4_COLOR,
                                     pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, (x + 1) * BLOCK_SIZE,
                                                 (y + 1) * BLOCK_SIZE))

            pygame.display.flip()
