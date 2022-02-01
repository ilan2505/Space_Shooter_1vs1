import pygame
import os


WIN=pygame.display.set_mode((900,500))
def main():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        WIN.fill((250,250,250))
        pygame.display.update()

    pygame.quit()
if __name__ == '__main__':
    main()