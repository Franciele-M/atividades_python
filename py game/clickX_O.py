#Título: Nomear a janela/Click na tela e aparece o X e Y e a cor do setup muda

#Lição de Casa: COMENTA TODAS AS LINHAS COM AS FUNÇÕES DESSE CÓDIGO!


import pygame #importa a biblioteca pygame para o script

# pygame configuração
pygame.init() #inicialização do pacote pygame
pygame.font.init()  #inicalização da fonte no pygame (init = inicio)
screen = pygame.display.set_mode((500, 500)) #configura o tamanho da tela
pygame.display.set_caption("Jogo da Velha") # Altera o título da janela
clock = pygame.time.Clock() #biblioteca tempo
running = True #variável de controle de status do jogo
cor_fundo = 1 #azul


fonte_quadrinhos = pygame.font.SysFont("Comic Sans MS", 30) #importando a fonte o definindo o tamanho dela


personagem_x = fonte_quadrinhos.render("X", True, "Pink")
personagem_y = fonte_quadrinhos.render("O", True, "Yellow")


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
            
            letra = "X" #quando o mouse é clicado o X aparece
        

    if cor_fundo == 1:
        screen.fill("blue")
        screen.blit(personagem_x,(250, 250))

    elif cor_fundo == 2:
        screen.fill("red")
        screen.blit(personagem_y,(250, 250))
    else:
        screen.fill("purple")


    
    # flip() the display to put your work on screen
    # display para atualizar a página
    pygame.display.flip()

    clock.tick(60)  # limita FPS para 60 / 60 fps por segundos. quanto mais fps por segundo, mas fluído fica a imagem; quanto menos, menor a qualidade

pygame.quit()