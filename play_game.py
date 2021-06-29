from game import Game
from player import Player
from ghost import *


def main(display=pygame.display.set_mode((W * BLOCK_SIZE, H * BLOCK_SIZE)),
         blinky: Ghost = Ghost(),
         pinky: Ghost = Ghost(),
         inky: Ghost = Ghost(),
         clyde: Ghost = Ghost()):
    game: Game = Game(display)
    player: Player = Player()
    while 1:
        game.draw()
        action = player.action()
        state = game.get_state()
        blinky_act = blinky.action(state)
        pinky_act = pinky.action(state)
        inky_act = inky.action(state)
        clyde_act = clyde.action(state)
        if game.step(action, blinky_act, pinky_act, inky_act, clyde_act):
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
    main(blinky=pinky(), pinky=blinky(), inky=pinky(), clyde=blinky())
