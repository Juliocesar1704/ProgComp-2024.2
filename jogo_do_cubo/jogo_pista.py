import pygame
import sys
import random

pygame.init()

# Dimensões da tela
altura_da_tela = 600
largura_da_tela = 1000
gameDisplay = pygame.display.set_mode((largura_da_tela, altura_da_tela))
pygame.display.set_caption("Corrida do Cubo")

# Lista de cores
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

# Carregar a imagem de fundo
fundo = pygame.image.load(r"C:\Users\david douglas\Downloads\space.JPEG")  
fundo = pygame.transform.scale(fundo, (largura_da_tela, altura_da_tela))  

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
    
    # Variável para controle do jogo
    ativo = True
    game_over = False

    while ativo:
        # Desenha a imagem de fundo
        gameDisplay.blit(fundo, (0, 0))  

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
                    # Obstáculo caindo do topo
                    obstaculo = pygame.Rect(random.randint(0, largura_da_tela - 40), 0, 40, 40)
                else:
                    # Obstáculo vindo da direita no chão
                    obstaculo = pygame.Rect(largura_da_tela, chao_y - 40, 40, 40)

                obstaculos.append(obstaculo)

            # Mover obstáculos
            for obstaculo in obstaculos:
                if obstaculo.y == 0:  # Obstáculos caindo
                    obstaculo.y += 300
                else:  # Obstáculos vindo da direita
                    obstaculo.x -= 5  # Agora realmente se move para a esquerda!

            # Verificar colisão
            for obstaculo in obstaculos:
                if pygame.Rect(cubo_x, cubo_y, cubo_largura, cubo_altura).colliderect(obstaculo):
                    game_over = True

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

        # Atualizar a tela
        pygame.display.update()

        # Controlar a taxa de quadros
        clock.tick(60)

# Rodar o jogo
game_loop()
