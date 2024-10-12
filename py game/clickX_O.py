#Título: Nomear a janela/Click na tela e aparece o X e O e a cor do setup muda


import pygame #importa a biblioteca pygame para o script

# pygame configuração
pygame.init() #inicialização do pacote pygame
pygame.font.init()  #inicalização da fonte no pygame (init = inicio)
screen = pygame.display.set_mode((500, 500)) #configura o tamanho da tela
pygame.display.set_caption("Jogo da Velha") # Altera o título da janela
clock = pygame.time.Clock() #biblioteca tempo
running = True #variável de controle de status do jogo
cor_fundo = 1 #azul / contador


fonte_quadrinhos = pygame.font.SysFont("Comic Sans MS", 30) #importando a fonte o definindo o tamanho dela

# Render = tranforma texto em imagem
personagem_x = fonte_quadrinhos.render("X", True, "Pink") #Renderiza o "X" e o deixa rosa
personagem_y = fonte_quadrinhos.render("O", True, "Yellow") #Renderiza o "O" e o deixa amarela

#Loop do jogo
while running: # Enquanto a variável "running" for verdadeira, o jogo continua

    #controle de enventos do jogo
    #pygame.QUIT significa quando o usuário clicar em X a tela fechará
    for event in pygame.event.get(): #verifica todos os eventos (tipo, click do mouse)
        if event.type == pygame.QUIT: #se clicar no X da janela (sair)
            running = False # Para o loop (fecha a janela)

        # Lógica para click
        # MOUSEBUTTONDOWN significa evento do click do mouse
        if event.type == pygame.MOUSEBUTTONDOWN: # Se o mouse for clicado
            print("Clicou!") # Aparecerá "clicou!" no terminal
            cor_fundo = cor_fundo + 1 #contador

            if(cor_fundo > 3): #se o contador for maior que 3
                cor_fundo = 1 # o contador volta a ser 1
            
            letra = "X" #quando o mouse é clicado o X aparece / define a variável como X
        
    # muda a cor e mostra as letras
    if cor_fundo == 1: # se o contador for = 1
        screen.fill("blue") # a tela fica azul
        screen.blit(personagem_x,(250, 250)) # posiciona o X na tela

    elif cor_fundo == 2: # se o contador for = 2
        screen.fill("red") # a tela fica vermelha
        screen.blit(personagem_y,(250, 250)) # posiciona o O na tela
    else: # caso contrario / não é 1 e nem 2, é 3
        screen.fill("purple") # a tela fica roxa


    
    # display para atualizar a página
    pygame.display.flip()

    clock.tick(60)  # limita FPS para 60 / 60 fps por segundos. quanto mais fps por segundo, mas fluído fica a imagem; quanto menos, menor a qualidade

pygame.quit() # Fecha o pygame e finaliza o jogo
