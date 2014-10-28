from __future__ import division

from maze import make_maze, Solver

def game(s):
    import pygame
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 255)
    clock = pygame.time.Clock()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))

    BLOCK_WIDTH = width / s.width
    BLOCK_HEIGTH = height / s.height

    def render():
        for y, row in enumerate(s.maze):
            for x, spot in enumerate(row):
                if (x, y) == s.current:
                    pygame.draw.rect(screen, GREEN, [x*BLOCK_WIDTH, y*BLOCK_HEIGTH, BLOCK_WIDTH, BLOCK_HEIGTH], 0)
                elif spot:
                    pygame.draw.rect(screen, WHITE, [x*BLOCK_WIDTH, y*BLOCK_HEIGTH, BLOCK_WIDTH, BLOCK_HEIGTH], 0)
                else:
                    pygame.draw.rect(screen, BLACK, [x*BLOCK_WIDTH, y*BLOCK_HEIGTH, BLOCK_WIDTH, BLOCK_HEIGTH], 0)
        pygame.display.flip()

    render()
    while True:
        if s.stop != s.current:
            s.update()
        render()
        clock.tick(10)


def main():
    m = make_maze(20, 20)
    s = Solver(m, (0, 0), (19, 19))
    print s
    while True:
        s.update()
        if s.stop == s.current:
            print 'yay'
            return True
        print s
        raw_input()

if __name__ == '__main__':
    #main()
    m = make_maze(20, 20)
    s = Solver(m, (0, 0), (19, 19))
    game(s)



