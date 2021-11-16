from game import Game
from ghosts.blinky import Blinky
from player import Player
from ghosts.ghost import *


def main(display=pygame.display.set_mode((W * BLOCK_SIZE, H * BLOCK_SIZE)),
         blinky: Ghost = Ghost(BLINKY, "blinky"),
         pinky: Ghost = Ghost(PINKY, "pinky"),
         inky: Ghost = Ghost(INKY, "inky"),
         clyde: Ghost = Ghost(CLYDE, "clyde")):
    ghost_names = [blinky, pinky, inky, clyde]
    game: Game = Game(display)
    player: Player = Player()
    while "false":
        game.draw()
        action = player.action()
        state = game.get_state()
        blinky_act = blinky.action(state, 1)
        pinky_act = pinky.action(state, 2)
        inky_act = inky.action(state, 3)
        clyde_act = clyde.action(state, 4)
        game_over = game.step(action, blinky_act, pinky_act, inky_act, clyde_act)
        if game_over:
            print(ghost_names[game_over - 1])
            break

    image = pygame.image.load("media/game_over_pac.png")
    image = pygame.transform.scale(image, (W * BLOCK_SIZE, H * BLOCK_SIZE))
    display.blit(image, (0, 0))
    text = FONT.render(f"Score: {game.score}", True, YELLOW)
    display.blit(text, ((W * BLOCK_SIZE - text.get_rect().width) / 2, (H - 2) * BLOCK_SIZE))
    pygame.display.flip()

    game_over_screen = True
    while game_over_screen:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over_screen = False


if __name__ == '__main__':
    blinky = Blinky(BLINKY)
    pinky = Random(PINKY, name='pinky')
    inky = Random(INKY, name='inky')
    clyde = Random(CLYDE, name='clyde')
    main(blinky=blinky, pinky=pinky, inky=inky, clyde=clyde)