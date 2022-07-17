import pygame

#colors

BLACK = (0,0,0)


# window set up
WIDTH, HIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Tic Tac Toe")



def main():

    #game loop
    RUN = True
    clock = pygame.time.Clock()
    FPS = 60



    while RUN :
        pygame.display.update()
        clock.tick(FPS)
        WIN.fill(BLACK)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                RUN = False
        

main()