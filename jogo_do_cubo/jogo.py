import pygame
import sys
import random

pygame.init()

# Dimensões da tela 
altura_da_tela = 600
largura_da_tela = 1000
gameDisplay = pygame.display.set_mode((largura_da_tela, altura_da_tela)) 
pygame.display.set_caption("Corrida do Cubo")

# Lista de cores em Duplas com 3 valores
cores = [
    (255, 255, 255),  # WHITE
    (0, 0, 0),        # BLACK
    (255, 0, 0),      # RED
    (0, 255, 0),      # GREEN
    (0, 0, 255),      # BLUE
    (255, 255, 0),    # YELLOW
    (0, 255, 255),    # CYAN
    (255, 0, 255),    # MAGENTA
    (255, 165, 0),    # ORANGE
    (128, 0, 128),    # PURPLE
    (165, 42, 42),    # BROWN
    (255, 105, 180),  # PINK
    (128, 128, 128),  # GRAY
]
# Fonte para exibir "Game Over"
fonte = pygame.font.Font(None, 50)

# Geração da soundtrack do game
musica_de_fundo1 = pygame.mixer.music.load('space.mp3')
pygame.mixer.music.play(-1)

# Carregar a imagem de fundo
fundo1 = pygame.image.load('fundo.jpg')  
fundo1 = pygame.transform.scale(fundo1, (largura_da_tela, altura_da_tela)) 


# Função para exibir as instruções na tela inicial
def exibir_instrucoes():
    instrucoes_font = pygame.font.Font(None, 50)
    gameDisplay.blit(fundo1, (0, 0)) # Fundo para as instruções

    texto_titulo = instrucoes_font.render("Bem-vindo ao Jogo da Corrida do Cubo!", True, (255, 255, 255))
    gameDisplay.blit(texto_titulo, (largura_da_tela // 20, altura_da_tela // 4))
    texto_instrucoes1 = instrucoes_font.render("Use as setas para movimentar o cubo:", True, (255, 255, 255))
    gameDisplay.blit(texto_instrucoes1, (largura_da_tela // 20, altura_da_tela // 4 + 50))
    texto_instrucoes2 = instrucoes_font.render("Seta para CIMA: Pular", True, (255, 255, 255))
    gameDisplay.blit(texto_instrucoes2, (largura_da_tela // 20, altura_da_tela // 4 + 100))
    texto_instrucoes3 = instrucoes_font.render("Seta para ESQUERDA/DIREITA: Mover", True, (255, 255, 255))
    gameDisplay.blit(texto_instrucoes3, (largura_da_tela // 20, altura_da_tela // 4 + 150))
    texto_instrucoes4 = instrucoes_font.render("Evite os obstáculos! Pressione ENTER para começar.", True, (255, 255, 255))
    gameDisplay.blit(texto_instrucoes4, (largura_da_tela // 20, altura_da_tela // 4 + 200))
    frase = instrucoes_font.render("See you space, player!", True, (255, 255, 255))
    gameDisplay.blit(frase, (largura_da_tela // 20, altura_da_tela // 4 + 250))

    pygame.display.update()

    # Esperar até que o jogador pressione Enter para começar
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Quando pressionar Enter
                    esperando = False

# Função principal do jogo
def game_loop():
    # Cores aleatórias
    cor_do_cubo = random.choice(cores)
    cor_do_chao = random.choice(cores)
    cor_do_teto = random.choice(cores)
    cor_obstaculo = random.choice(cores)

    # Variáveis do cubo
    cubo_x = 50
    cubo_y = altura_da_tela - 100
    cubo_largura = 40
    cubo_altura = 40
    velocidade_x = 0
    gravidade = 0.5
    velocidade_y = 0
    pulo = -10
    no_chao = True
    velocidade_cubo = 5

    # Variáveis dos obstáculos
    obstaculos = []
    tempo_entre_obstaculos = 50
    contador_obstaculo = 0

    # Base do chão e altura do teto
    base = 100
    chao_y = altura_da_tela - base
    teto_altura = 40

# Relógio do jogo
    clock = pygame.time.Clock()
    
    ################################################### 2
    # Variável para controle do jogo
    jogando = True
    game_over = False
    while jogando:
        # Desenha a imagem de fundo
        gameDisplay.blit(fundo1, (0, 0))  
           
        # Processar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_over:
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                    game_loop()  # Reinicia o jogo

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and no_chao:
                    velocidade_y = pulo
                    no_chao = False
                if evento.key == pygame.K_LEFT:
                    velocidade_x = -velocidade_cubo
                if evento.key == pygame.K_RIGHT:
                    velocidade_x = velocidade_cubo
                if evento.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()

            if evento.type == pygame.KEYUP:
                if evento.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    velocidade_x = 0

        if not game_over:
            # Aplicar gravidade
            velocidade_y += gravidade
            cubo_y += velocidade_y

            # Movimentar o cubo
            cubo_x += velocidade_x

            # Impedir que o cubo saia da tela
            cubo_x = max(0, min(cubo_x, largura_da_tela - cubo_largura))

            # Evitar que o cubo caia do chão
            if cubo_y >= chao_y - cubo_altura:
                cubo_y = chao_y - cubo_altura
                no_chao = True
                velocidade_y = 0

            # Gerar obstáculos aleatórios
            contador_obstaculo += 1
            if contador_obstaculo >= tempo_entre_obstaculos:
                contador_obstaculo = 0
                tipo = random.choice(["cima", "direita"])

                if tipo == "cima":
                    # Obstáculo caindo do topo ou eixo Y
                    # largura_da_tela-40 para que o obstaculo não ultrapasse o eixo  X da tela gerado no eixo Y
                    obstaculo = pygame.Rect(random.randint(0, largura_da_tela - 40), 0, 40, 40)
                else:
                    # Obstáculo vindo da direita no chão ou no eixo X
                    # chao_y-40 é para que o obstaculo não saia da base no eixo Y do jogo 40x40 pixel 
                    obstaculo = pygame.Rect(largura_da_tela, chao_y - 40, 40, 40)

                obstaculos.append(obstaculo)

            # Mover obstáculos
            for obstaculo in obstaculos:
                if obstaculo.y == 0:  # Obstáculos sendo gerados na cordenada 0 do eixo Y
                    obstaculo.y += 300 # Faz com que ele se mova para baixo ate a posição 300
                else:  # Obstáculos vindo da direita
                    obstaculo.x -= 5  # Agora se não for constado no eixo Y gera no eixo X movendo ele para a esquerda

            # Verificar colisão
            for obstaculo in obstaculos:
                if pygame.Rect(cubo_x, cubo_y, cubo_largura, cubo_altura).colliderect(obstaculo):
                    game_over = True
########################################################## 3
        # Desenhar o chão e o teto
        pygame.draw.rect(gameDisplay, cor_do_chao, (0, chao_y, largura_da_tela, base))
        pygame.draw.rect(gameDisplay, cor_do_teto, (0, 0, largura_da_tela, teto_altura))

        # Desenhar cubo e obstáculos
        pygame.draw.rect(gameDisplay, cor_do_cubo, (cubo_x, cubo_y, cubo_largura, cubo_altura))
        for obstaculo in obstaculos:
            pygame.draw.rect(gameDisplay, cor_obstaculo, obstaculo)

        # Se o jogador perder, exibir "Game Over"
        if game_over:
            texto_game_over = fonte.render("Acho que perdeu!", True, (255, 0, 0))
            gameDisplay.blit(texto_game_over, (largura_da_tela // 4, altura_da_tela // 2))
            texto_reiniciar = fonte.render("Pressione R para reiniciar", True, (255, 255, 255))
            gameDisplay.blit(texto_reiniciar, (largura_da_tela // 4, altura_da_tela // 2 + 50))
            texto_sair = fonte.render("Caso queira desisitir aperte a tecla Espaço",True,(255, 255, 255))
            gameDisplay.blit(texto_sair, (largura_da_tela // 4, altura_da_tela // 2 + 100))
        # Atualizar a tela
        pygame.display.update()

        # Controlar a taxa de quadros
        clock.tick(60)

# Exibir instruções
exibir_instrucoes() 

# Rodar o jogo
game_loop()
