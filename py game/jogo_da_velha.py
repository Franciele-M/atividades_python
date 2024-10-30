#Título: Jogo da Velha - Minha Lógica


import pygame #importa a biblioteca pygame para o script

# pygame configuração
pygame.init() #inicialização do pacote pygame
pygame.font.init()  #inicalização da fonte no pygame (init = inicio)
screen = pygame.display.set_mode((600, 600)) #configura o tamanho da tela
pygame.display.set_caption("Jogo da Velha") # Altera o título da janela
clock = pygame.time.Clock() #biblioteca tempo

#q1 = (x > 0) and (x < 200) and (y < 200)
#q2 = (x >= 200) and (x < 400) and (y < 200)


running = True #variável de controle de status do jogo
cor_fundo = 1 #azul / contador
rodadas = 0
tabuleiro_desenhado = False
x = 0
y = 0

fonte_mensagem = pygame.font.SysFont("Comic Sans MS", 150)

mensagem1 = fonte_mensagem.render("Game ", True, "Yellow")
mensagem2 = fonte_mensagem.render("Over! ", True, "Yellow")



fonte_quadrinhos = pygame.font.SysFont("Comic Sans MS", 80) #importando a fonte o definindo o tamanho dela

# Render = tranforma texto em imagem
personagem_x = fonte_quadrinhos.render("X", True, "Blue") #Renderiza o "X" e o deixa rosa
personagem_o = fonte_quadrinhos.render("O", True, "Purple") #Renderiza o "O" e o deixa amarela

#variável do personagem atual
personagem_atual = personagem_o




# Dicionário para armazenar o estado dos quadrantes
quadrantes = {
    "q1": None,
    "q2": None,
    "q3": None,
    "q4": None,
    "q5": None,
    "q6": None,
    "q7": None,
    "q8": None,
    "q9": None,
}






 # função ...        (aqui é a variável)
def desenha_tabuleiro(espessura, cor):
    # valor 7 = espesu
     # Desenho do tabuleiro
        #                                  Origem    Destino
        #                                 ( x, y ) ( x ,  y )
        pygame.draw.line(screen, cor,(200, 0), (200, 600), espessura) # desenha uma linha vertical na tela (variável: tela, cor, tamanho, tamanho, expessura)
        pygame.draw.line(screen, cor,(400, 0), (400, 600), espessura) # desenha uma linha vertical na tela (variável: tela, cor, tamanho, tamanho, expessura)
       
       #                                  3º  1º  ,  4º  , 2º   quadrante
        pygame.draw.line(screen, cor,(0, 200), (600, 200), espessura) # desenha uma linha vertical na tela (variável: tela, cor, tamanho, tamanho, expessura)
        pygame.draw.line(screen, cor,(0, 400), (600, 400), espessura) # desenha uma linha vertical na tela (variável: tela, cor, tamanho, tamanho, expessura)



def faz_jogada():
     #         Jogadores:      Eixo  x , y

        if q1 = True: # Primeiro
            screen.blit(personagem_atual, (70, 40)) # 1/1

        elif q2 = True: # Segundo
            screen.blit(personagem_atual, (270, 40)) # 2/1

        elif x >= 400 and y < 200: # Terceiro
            screen.blit(personagem_atual, (470, 40)) # 3/1

        elif x < 200 and y >= 200 and y < 400: # Quarto
            screen.blit(personagem_atual, (70, 240)) # 1/2
            
        elif x >= 200 and x < 400 and y >= 200 and y < 400: # Quinto
            screen.blit(personagem_atual, (270, 240)) # 2/2

        elif x >= 400 and y >= 200 and y < 400: # Sexto
            screen.blit(personagem_atual, (470, 240)) # 3/2

        elif x < 200 and y >= 400: # Sétimo
            screen.blit(personagem_atual, (70, 440)) # 1/3

        elif x >= 200 and x < 400 and y >= 400: # Oitavo
            screen.blit(personagem_atual, (270, 440)) # 2/3

        elif x >= 400 and y >= 400: # Nono
            screen.blit(personagem_atual, (470, 440)) # 3/3
            #screen.blit(mensagem1, (100, 50)) # 3/3
            #screen.blit(mensagem2, (100, 250)) # 3/3




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
            #print("Clicou!") # Aparecerá "clicou!" no terminal
            click_pos = pygame.mouse.get_pos() # traz a posição do mouse no evento click

            print("Eixo X: ", click_pos[0])
            print("Eixo Y: ", click_pos[1])
            x = click_pos[0]
            y = click_pos[1]
            
            rodadas = rodadas + 1 #contador
            print(rodadas)

            # if(rodadas > 11): #se o contador for maior que 10
            #     rodadas = 0 # o contador volta a ser 1
            
            #letra = "X" #quando o mouse é clicado o X aparece / define a variável como X
            # x,y = pygame.mouse.get_pos()

            

            # Altera o persnagem de X para O
            if personagem_atual == personagem_o:
                personagem_atual = personagem_x

            else:
                personagem_atual = personagem_o


            faz_jogada() # ACRESCENTAR 


        if tabuleiro_desenhado == False:
            #Função que desenha tabuleiro (espessura, cor) (aqui é o valor da variável: tamanho, cor, etc.)
            desenha_tabuleiro(10, "green")
            tabuleiro_desenhado = True #DESCOMENTA DEPOIS

        

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

       
        if rodadas >= 10:
            screen.fill("Black")
            rodadas = 0
            x = 0
            y = 0
            tabuleiro_desenhado = False #DESCOMENTA DEPOIS



            # Redesenha o tabuleiro
        #     pygame.draw.line(screen, "white",(200, 0), (200, 600), 7) # desenha uma linha vertical na tela (variável: tela, cor, tamanho, tamanho, expessura)
        #     pygame.draw.line(screen, "white",(400, 0), (400, 600), 7) # desenha uma linha vertical na tela (variável: tela, cor, tamanho, tamanho, expessura)
        
        # #                                  3º  1º  ,  4º  , 2º   quadrante
        #     pygame.draw.line(screen, "white",(0, 200), (600, 200), 7) # desenha uma linha vertical na tela (variável: tela, cor, tamanho, tamanho, expessura)
        #     pygame.draw.line(screen, "white",(0, 400), (600, 400), 7) # desenha uma linha vertical na tela (variável: tela, cor, tamanho, tamanho, expessura)


#------------------------------GAME OVER!!!------------------------------------------

       if 

       
            

        

    # muda a cor e mostra as letras
    #if cor_fundo == 1: # se o contador for = 1
      #  screen.blit(personagem_x,(20, 20)) # posiciona o X na tela

    #elif cor_fundo == 2: # se o contador for = 2
        # screen.fill("red") # a tela fica vermelha
       # screen.blit(personagem_o,(250, 250)) # posiciona o O na tela

    
    # display para atualizar a página
    pygame.display.flip()

    clock.tick(60)  # limita FPS para 60 / 60 fps por segundos. quanto mais fps por segundo, mas fluído fica a imagem; quanto menos, menor a qualidade

pygame.quit() # Fecha o pygame e finaliza o jogo
