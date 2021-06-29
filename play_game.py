from game import Game
from player import Player
from ghost import *


def main(display=pygame.display.set_mode((W * BLOCK_SIZE, H * BLOCK_SIZE)),
         g1: Ghost = Ghost(),
         g2: Ghost = Ghost(),
         g3: Ghost = Ghost(),
         g4: Ghost = Ghost()):
    game: Game = Game(display)
    player: Player = Player()
    while 1:
        game.draw()
        action = player.action()
        state = game.get_state()
        g1_act = g1.action(state)
        g2_act = g2.action(state)
        g3_act = g3.action(state)
        g4_act = g4.action(state)
        if game.step(action, g1_act, g2_act, g3_act, g4_act):
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
    main(g1=G2(), g2=G1(), g3=G2(), g4=G1())
