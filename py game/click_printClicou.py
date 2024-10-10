# Example file showing a basic pygame "game loop"
#Titulo: Click na tela e veja a mensagem
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
cor_fundo = 3 #azul



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #fill = preencher
   # screen.fill("blue")

    # RENDER YOUR GAME HERE / add a lógica

    
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Clicou!")


    # if cor_fundo == 1:
    #     screen.fill("blue")

    # elif cor_fundo == 2:
    #     screen.fill("red")
    # else:
    #     screen.fill("purple")


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60 / 60 fps por segundos. quanto mais fps por segundo, mas fluído fica a imagem; quanto menos, menor a qualidade

pygame.quit()