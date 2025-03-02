import pygame
import sys
import random

# Inicialização do pygame
pygame.init()

# Configurações da tela
altura_da_tela = 800
largura_da_tela = 1000
gameDisplay = pygame.display.set_mode((largura_da_tela, altura_da_tela))
pygame.display.set_caption("Jogo de Pulo")

# Cores
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
    (0, 128, 128),    # TEAL
    (128, 128, 0),    # OLIVE
    (106, 90, 205),   # SLATEBLUE
    (255, 215, 0),    # GOLD
    (230, 230, 250),  # LAVENDER
    (255, 218, 185),  # PEACH
    (189, 252, 201),  # MINT
    (255, 182, 193),  # LIGHTPINK
    (135, 206, 235),  # SKYBLUE
    (255, 255, 224),  # LIGHTYELLOW
    (144, 238, 144),  # LIGHTGREEN
    (169, 169, 169),  # DARKGRAY
    (211, 211, 211),  # LIGHTGRAY
    (192, 192, 192),  # SILVER
    (105, 105, 105)   # DIMGRAY
]

# Escolher cores aleatórias para o cubo e o fundo
cor_do_cubo = random.choice(cores)
cor_de_fundo = random.choice(cores)
cor_do_blok = random.choice(cores)
cor_do_chao = random.choice(cores)
cor_do_teto = random.choice(cores)

# Configurações do cubo (jogador)
cubo_x = 50
cubo_y = altura_da_tela - 100
cubo_largura = 40
cubo_altura = 40
velocidade_pulo = -10
gravidade = 0.5
velocidade_x = 0
velocidade_y = 0
no_chao = True
pulo = -10
velocidade_maxima = 20
aceleracao = 0.5  # Aceleração para o movimento

# Configurações do chão
base = 100
chao_y = altura_da_tela - base
teto_altura = 40

# Configurações dos obstáculos
largura_obstaculo = 60
altura_max_obstaculo = 300
velocidade_obstaculos = 5
obstaculos = []

# Função para gerar obstáculos
def gerar_obstaculos():
    nova_altura_chao = random.randint(50, altura_max_obstaculo)
    nova_altura_teto = random.randint(50, altura_max_obstaculo)
    obstaculos.append([largura_da_tela, chao_y - nova_altura_chao, largura_obstaculo, nova_altura_chao])
    obstaculos.append([largura_da_tela, 0, largura_obstaculo, nova_altura_teto])

# Função para desenhar o cubo (jogador)
def desenho_cubo():
    pygame.draw.rect(gameDisplay, cor_do_cubo, (cubo_x, cubo_y, cubo_largura, cubo_altura))

# Função principal do jogo
def game_loop():
    global cubo_x, cubo_y, velocidade_y, no_chao, velocidade_x, obstaculos

    # Inicializar o jogo
    gerar_obstaculos()
    
    clock = pygame.time.Clock()

    # Loop do jogo
    ativo = True
    while ativo:
        # Preencher a tela com a cor de fundo
        gameDisplay.fill(cor_de_fundo)

        # Processar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and no_chao:
                    velocidade_y = pulo
                    no_chao = False
            elif evento.type == pygame.KEYUP:
                if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    velocidade_x = 0  # Para o movimento ao soltar a tecla

        # Captura teclas pressionadas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            velocidade_x -= aceleracao  # Aumenta a velocidade para a esquerda
            if velocidade_x < -velocidade_maxima:
                velocidade_x = -velocidade_maxima
        if keys[pygame.K_RIGHT]:
            velocidade_x += aceleracao  # Aumenta a velocidade para a direita
            if velocidade_x > velocidade_maxima:
                velocidade_x = velocidade_maxima

        # Atualizar a posição do cubo (gravidade)
        velocidade_y += gravidade
        cubo_y += velocidade_y
        cubo_x += velocidade_x

        # Impedir que o cubo ultrapasse o chão
        if cubo_y + cubo_altura >= chao_y:
            cubo_y = chao_y - cubo_altura
            velocidade_y = 0
            no_chao = True

        # Impedir que o cubo saia da tela para os lados
        if cubo_x < 0:
            cubo_x = 0
        if cubo_x + cubo_largura > largura_da_tela:
            cubo_x = largura_da_tela - cubo_largura

        # Movimentação e geração de obstáculos
        for obstaculo in obstaculos:
            obstaculo[0] -= velocidade_obstaculos  # Move os obstáculos para a esquerda

        # Remove obstáculos que saíram da tela e adiciona novos
        if obstaculos and obstaculos[0][0] < -largura_obstaculo:
            obstaculos.pop(0)  # Remove obstáculo do chão
            obstaculos.pop(0)  # Remove obstáculo do teto
            gerar_obstaculos()  # Adiciona novos obstáculos no final da tela

        # Colisão com obstáculos
        for obstaculo in obstaculos:
            if (cubo_x < obstaculo[0] + obstaculo[2] and
                cubo_x + cubo_largura > obstaculo[0] and
                cubo_y < obstaculo[1] + obstaculo[3] and
                cubo_y + cubo_altura > obstaculo[1]):
                print("Colisão! Reiniciando...")
                pygame.time.delay(1000)
                cubo_x = 50
                cubo_y = altura_da_tela - 100
                velocidade_x = 0
                velocidade_y = 0
                obstaculos.clear()
                gerar_obstaculos()

        # Desenha o cubo (jogador)
        desenho_cubo()

        # Desenha o chão e o teto
        pygame.draw.rect(gameDisplay, cor_do_chao, (0, chao_y, largura_da_tela, base))
        pygame.draw.rect(gameDisplay, cor_do_teto, (0, 0, largura_da_tela, teto_altura))

        # Desenha os obstáculos
        for obstaculo in obstaculos:
            pygame.draw.rect(gameDisplay, cor_do_blok, (obstaculo[0], obstaculo[1], obstaculo[2], obstaculo[3]))

        # Atualiza a tela
        pygame.display.update()

        # Controla a taxa de quadros por segundo
        clock.tick(60)

# Rodar o loop do jogo
game_loop()
