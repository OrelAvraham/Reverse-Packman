from game import Game
from player import Player
from ghost import *

display = pygame.display.set_mode((W * BLOCK_SIZE, H * BLOCK_SIZE))
game: Game = Game(display)
player: Player = Player()
g1: Ghost = Ghost()
g2: Ghost = Ghost()
g3: Ghost = Ghost()
g4: Ghost = Ghost()

while 1:
    game.draw()
    action = player.action()
    state = game.get_state()
    g1_act = g1.action(state)
    g2_act = g2.action(state)
    g3_act = g3.action(state)
    g4_act = g4.action(state)
    if game.step(action, g1_act, g2_act, g3_act, g4_act):
        game.game_over()
    game.score += 1


if __name__ == '__main__':
    pass
