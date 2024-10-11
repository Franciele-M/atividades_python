#Título: mude a cor da tela com um click

# Example file showing a basic pygame "game loop"
#Titulo: Click na tela e veja a mensagem e mude de cor do setup
#Título: Nomear a janela

#Lição de Casa: COMENTA TODAS AS LINHAS COM AS FUNÇÕES DESSE CÓDIGO!




# Example file showing a basic pygame "game loop"
#Titulo: Click na tela e veja a mensagem e mude de cor do setup
import pygame #importa a biblioteca pygame para o script

# pygame configuração
pygame.init() #inicialização do pacote pygame
screen = pygame.display.set_mode((500, 500)) #configura o tamanho da tela
clock = pygame.time.Clock() #biblioteca tempo
running = True #variável de controle de status do jogo
cor_fundo = 1 #azul

# Altera o título da janela
pygame.display.set_caption("Jogo da Velha")

while running:
    #controle de enventos do jogo
    #pygame.QUIT significa quando o usuário clicar em X a tela fechará
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Lógica
        # MOUSEBUTTONDOWN significa evento do click do mouse
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
    # display para atualizar a página
    pygame.display.flip()

    clock.tick(60)  # limita FPS para 60 / 60 fps por segundos. quanto mais fps por segundo, mas fluído fica a imagem; quanto menos, menor a qualidade

pygame.quit()