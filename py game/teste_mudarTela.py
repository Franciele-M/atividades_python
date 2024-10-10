# Example file showing a basic pygame "game loop"
#Titulo: Tela azul
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #fill = preencher
    screen.fill("blue")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60 / 60 fps por segundos. quanto mais fps por segundo, mas fluído fica a imagem; quanto menos, menor a qualidade

pygame.quit()