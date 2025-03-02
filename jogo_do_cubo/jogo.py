import pygame
import sys
import random

pygame.init()
altura_da_tela = 800
largura_da_tela = 1000
gameDisplay = pygame.display.set_mode((largura_da_tela, altura_da_tela))
pygame.display.set_caption("Jogo de Pulo")

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


cor_do_cubo = random.choice(cores)
cor_de_fundo = random.choice(cores)
print(cor_do_cubo)
print(cor_de_fundo)

# Variáveis do cubo e movimento
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

# Inicializar o relógio
clock = pygame.time.Clock()

# Função para desenhar o cubo
def desenho_cubo():
    pygame.draw.rect(gameDisplay, cor_do_cubo, (cubo_x, cubo_y, cubo_largura, cubo_altura))


# Função de movimentação e lógica do jogo
def game_loop():
    global cubo_y, velocidade_y, no_chao, cubo_x
    
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
                elif evento.key == pygame.K_LEFT:
                    cubo_x -= 10
                elif evento.key == pygame.K_RIGHT:
                    cubo_x += 10
        keys = pygame.key.get_pressed()
        if keys [pygame.K_LEFT]:
            velocidade_x = velocidade_maxima
            cubo_x -= 10

        if keys [pygame.K_RIGHT]:
            velocidade_x = velocidade_maxima
            cubo_x += 10
            
        # Atualizar a posição do cubo (gravidade)
        velocidade_y += gravidade
        cubo_y += velocidade_y

        # Impedir que o cubo ultrapasse o chão
        if cubo_y >= altura_da_tela - cubo_altura:
            cubo_y = altura_da_tela - cubo_altura
            no_chao = True
            velocidade_y = 0
        
        # Desenhar o cubo
        desenho_cubo()

        base = 100
        chao_y = altura_da_tela - base
        teto_altura = 40

        # Atualizar a tela
        pygame.display.update()

        # Controlar a taxa de quadros por segundo
        clock.tick(60)

# Rodar o loop do jogo
game_loop()


        
