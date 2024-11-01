#Título: Jogo da Velha - Lógica em Sala de Aula 


import pygame #importa a biblioteca pygame para o script

# pygame configuração
pygame.init() #inicialização do pacote pygame
pygame.font.init()  #inicalização da fonte no pygame (init = inicio)
screen = pygame.display.set_mode((600, 600)) #configura o tamanho da tela
pygame.display.set_caption("Jogo da Velha") # Altera o título da janela
clock = pygame.time.Clock() #biblioteca tempo
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
personagem_atual = personagem_x

#quadrantes
q1 = ''
q2 = ''
q3 = ''
q4 = ''
q5 = ''
q6 = ''
q7 = ''
q8 = ''
q9 = ''


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
    #             Jogadores:      Eixo  x , y
    global q1, q2, q3, q4, q5, q6, q7, q8, q9
    status = True

    if q1 == '' and x > 0 and x < 200 and y < 200: # Primeiro
        screen.blit(personagem_atual, (70, 40)) # 1/1
        q1 = personagem_atual

    elif q2 == '' and x >= 200 and x < 400 and y < 200: # Segundo
        screen.blit(personagem_atual, (270, 40)) # 2/1
        q2 = personagem_atual

    elif q3 == '' and x >= 400 and y < 200: # Terceiro
        screen.blit(personagem_atual, (470, 40)) # 3/1
        q3 = personagem_atual

    elif q4 == '' and x < 200 and y >= 200 and y < 400: # Quarto
        screen.blit(personagem_atual, (70, 240)) # 1/2
        q4 = personagem_atual
        
    elif q5 == '' and x >= 200 and x < 400 and y >= 200 and y < 400: # Quinto
        screen.blit(personagem_atual, (270, 240)) # 2/
        q5 = personagem_atual

    elif q6 == '' and x >= 400 and y >= 200 and y < 400: # Sexto
        screen.blit(personagem_atual, (470, 240)) # 3/2
        q6 = personagem_atual

    elif q7 == '' and x < 200 and y >= 400: # Sétimo
        screen.blit(personagem_atual, (70, 440)) # 1/3
        q7 = personagem_atual

    elif q8 == '' and x >= 200 and x < 400 and y >= 400: # Oitavo
        screen.blit(personagem_atual, (270, 440)) # 2/3
        q8 = personagem_atual

    elif q9 == '' and x >= 400 and y >= 400: # Nono
        screen.blit(personagem_atual, (470, 440)) # 3/3
        q9 = personagem_atual

        #screen.blit(mensagem1, (100, 50)) # 3/3
        #screen.blit(mensagem2, (100, 250)) # 3/3

    else:
        status = False

    return status


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

            if rodadas >= 9:
                screen.fill("Black")
                rodadas = 0
                x = 0
                y = 0
                tabuleiro_desenhado = False 

            if (faz_jogada()):
                rodadas = rodadas + 1 #contador
                 # Altera o persnagem de X para O
                if personagem_atual == personagem_x:
                    personagem_atual = personagem_o
                else:
                    personagem_atual = personagem_x




#--------------------------------------------------------------------------------------------------------------------------------------------------------------

       
        
    
       



    if tabuleiro_desenhado == False:
        #Função que desenha tabuleiro (espessura, cor) (aqui é o valor da variável: tamanho, cor, etc.)
        desenha_tabuleiro(10, "green")
        q1 = ''
        q2 = ''
        q3 = ''
        q4 = ''
        q5 = ''
        q6 = ''
        q7 = ''
        q8 = ''
        q9 = ''
        tabuleiro_desenhado = True #DESCOMENTA DEPOIS
       

        



#---------------GAME OVER!!!------------------------------------------

       

       
            
    # display para atualizar a página
    pygame.display.flip()

    clock.tick(60)  # limita FPS para 60 / 60 fps por segundos. quanto mais fps por segundo, mas fluído fica a imagem; quanto menos, menor a qualidade

pygame.quit() # Fecha o pygame e finaliza o jogo
