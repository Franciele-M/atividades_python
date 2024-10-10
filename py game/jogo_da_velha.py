#Título: faça um jogo da velha (nem começou)


import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
cor_fundo = 1 #azul



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Lógica
        if event.type == pygame.MOUSEBUTTONDOWN: #mousebuttondown = click do mouse
            print("Clicou!")
            cor_fundo = cor_fundo + 1 #contador

            if(cor_fundo > 3):
                cor_fundo = 1
        

    if cor_fundo == 1:
        screen.fill("blue")

    elif cor_fundo == 2:
        screen.fill("red")
    else:
        screen.fill("purple")


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60 / 60 fps por segundos. quanto mais fps por segundo, mas fluído fica a imagem; quanto menos, menor a qualidade

pygame.quit()

