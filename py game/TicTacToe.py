import pygame  # Importa a biblioteca pygame para o script

# pygame configuração
pygame.init()  # Inicialização do pacote pygame
pygame.font.init()  # Inicialização da fonte no pygame (init = início)
screen = pygame.display.set_mode((600, 600))  # Configura o tamanho da tela
pygame.display.set_caption("Jogo da Velha")  # Altera o título da janela
clock = pygame.time.Clock()  # Biblioteca tempo
running = True  # Variável de controle de status do jogo
cor_fundo = 1  # Azul / contador

# Fonte e renderização de "X" e "O"
fonte_quadrinhos = pygame.font.SysFont("Comic Sans MS", 70)  # Importando a fonte e definindo o tamanho dela
personagem_x = fonte_quadrinhos.render("X", True, "Blue")  # Renderiza o "X" e o deixa azul
personagem_y = fonte_quadrinhos.render("O", True, "Purple")  # Renderiza o "O" e o deixa roxo

# Variáveis para o jogo da velha
tabuleiro = ["", "", "", "", "", "", "", "", ""]  # Lista para armazenar as jogadas
jogador_atual = "X"  # Define o jogador atual como "X"
jogadas = 0  # Contador de jogadas

# Função para desenhar o tabuleiro
def desenha_tabuleiro():
    pygame.draw.line(screen, "white", (200, 0), (200, 600), 10)  # Linha vertical à esquerda
    pygame.draw.line(screen, "white", (400, 0), (400, 600), 10)  # Linha vertical à direita
    pygame.draw.line(screen, "white", (0, 200), (600, 200), 10)  # Linha horizontal superior
    pygame.draw.line(screen, "white", (0, 400), (600, 400), 10)  # Linha horizontal inferior

# Função para posicionar X e O no tabuleiro
def desenha_jogadas():
    for i in range(9):  # Percorre as 9 posições do tabuleiro
        x_pos = (i % 3) * 200 + 60  # Calcula a posição X de cada quadrado
        y_pos = (i // 3) * 200 + 30  # Calcula a posição Y de cada quadrado
        if tabuleiro[i] == "X":
            screen.blit(personagem_x, (x_pos, y_pos))  # Desenha o "X"
        elif tabuleiro[i] == "O":
            screen.blit(personagem_y, (x_pos, y_pos))  # Desenha o "O"

# Função para verificar se o jogo acabou
def verifica_fim_de_jogo():
    global running
    if jogadas == 9:  # Se as 9 jogadas forem realizadas, o jogo termina
        print("Game Over")  # Exibe "Game Over" no terminal
        running = False  # Para o jogo

# Loop do jogo
while running:  # Enquanto a variável "running" for verdadeira, o jogo continua

    screen.fill("black")  # Preenche o fundo da tela com preto
    desenha_tabuleiro()  # Desenha o tabuleiro na tela
    desenha_jogadas()  # Desenha X e O no tabuleiro

    # Controle de eventos do jogo
    for event in pygame.event.get():  # Verifica todos os eventos (tipo, click do mouse)
        if event.type == pygame.QUIT:  # Se clicar no X da janela (sair)
            running = False  # Para o loop (fecha a janela)

        # Lógica para click
        if event.type == pygame.MOUSEBUTTONDOWN:  # Se o mouse for clicado
            print("Clicou!")  # Aparecerá "clicou!" no terminal
            x, y = pygame.mouse.get_pos()  # Captura a posição do clique
            posicao = (x // 200) + (y // 200) * 3  # Calcula a célula clicada (0 a 8)

            # Se a célula clicada estiver vazia
            if tabuleiro[posicao] == "":
                tabuleiro[posicao] = jogador_atual  # Marca o "X" ou "O" no tabuleiro
                jogadas += 1  # Aumenta o contador de jogadas

                # Alterna entre X e O
                if jogador_atual == "X":
                    jogador_atual = "O"  # Troca para o jogador O
                else:
                    jogador_atual = "X"  # Troca para o jogador X

                verifica_fim_de_jogo()  # Verifica se o jogo terminou

    # Atualiza a tela com as mudanças
    pygame.display.flip()

    # Limita os frames por segundo
    clock.tick(60)  # Limita FPS para 60

# Finaliza o pygame e o jogo
pygame.quit()
