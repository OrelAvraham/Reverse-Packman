from game_constants import *
from game import Game
from player import Player

display = pygame.display.set_mode((W * BLOCK_SIZE, H * BLOCK_SIZE))
game: Game = Game(display)
player: Player = Player()

while 1:
    game.draw()
    action = player.action()
    game.step(action, STAY, STAY, STAY, STAY)

if __name__ == '__main__':
    pass
