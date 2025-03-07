import pygame  # Importa a biblioteca pygame para o desenvolvimento do jogo
import sys  # Para manipulação do sistema (fechar o jogo)
import random  # Para gerar números aleatórios (utilizado para gerar obstáculos e cores)

pygame.init()  # Inicializa todos os módulos do pygame

# Dimensões da tela do jogo
altura_da_tela = 600  # Altura da tela do jogo
largura_da_tela = 1000  # Largura da tela do jogo
gameDisplay = pygame.display.set_mode((largura_da_tela, altura_da_tela))  # Cria a tela do jogo
pygame.display.set_caption("Cube Space Run")  # Define o título da janela

# Lista de cores em formato RGB (cada tupla representa uma cor)
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

# Fonte para exibir as mensagems
fonte = pygame.font.Font(None, 50)

# Geração da soundtrack do jogo
musica_de_fundo1 = pygame.mixer.music.load('space.mp3')  # Carrega a música de fundo
pygame.mixer.music.play(-1)  # Toca a música de fundo infinitamente

# Carregar a imagem de fundo e ajustar o tamanho
fundo1 = pygame.image.load('fundo.jpg') 
fundo1 = pygame.transform.scale(fundo1, (largura_da_tela, altura_da_tela)) 

# Função para exibir uma mensagem na tela
def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)  # Define a fonte para o texto sendo o tamanho e negrito e italico 
    mensagem = f'{msg}'  # A mensagem que será exibida
    texto_formatado = fonte.render(mensagem, True, cor)  # Renderiza a mensagem
    return texto_formatado  # Retorna a imagem do texto renderizado

# Função para exibir as instruções na tela inicial
def exibir_instrucoes():
    instrucoes_font = pygame.font.Font(None, 50)  # Define a fonte para as instruções
    gameDisplay.blit(fundo1, (0, 0))  # Exibe o fundo na tela

    # Exibe o título e as instruções do jogo
    texto_titulo = instrucoes_font.render("Bem-vindo ao Jogo da Corrida do Cubo!", True, (255, 255, 255)) # Renderiza o texto com true para negrito e a tupla com o valor das cores
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

    pygame.display.update()  # Atualiza a tela com as instruções

    # Espera até que o jogador pressione ENTER para começar o jogo
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Encerra o jogo quando a janela é fechada
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Quando pressionar ENTER
                    esperando = False  # Sai do loop e começa o jogo

# Função principal do jogo
def game_loop():
    cor_do_cubo = random.choice(cores)  # Cor do cubo (aleatória)
    cor_do_chao = random.choice(cores)  # Cor do chão (aleatória)
    cor_do_teto = random.choice(cores)  # Cor do teto (aleatória)
    cor_obstaculo = random.choice(cores)  # Cor dos obstáculos (aleatória)

    # Variáveis do cubo
    cubo_x = 50  # Posição inicial do cubo no eixo X
    cubo_y = altura_da_tela - 100  # Posição inicial do cubo no eixo Y (em relação ao chão)
    cubo_largura = 40  # Largura do cubo
    cubo_altura = 40  # Altura do cubo
    velocidade_x = 0  # Velocidade de movimento no eixo X
    gravidade = 0.5  # Força da gravidade
    velocidade_y = 0  # Velocidade de movimento no eixo Y
    pulo = -10  # A força do pulo
    no_chao = True  # Verifica se o cubo está no chão
    velocidade_cubo = 5  # Velocidade de movimentação do cubo

    # Variáveis dos obstáculos
    obstaculos = []  # Lista para armazenar os obstáculos
    tempo_entre_obstaculos = 50  # Tempo entre a geração de novos obstáculos
    contador_obstaculo = 0  # Contador de tempo para gerar obstáculos

    # Base do chão e altura do teto
    base = 100  # Altura da base do chão
    chao_y = altura_da_tela - base  # Posição Y do chão
    teto_altura = 40  # Altura do teto

    # Relógio do jogo para controlar o FPS
    clock = pygame.time.Clock()

    pontos = 0  # Inicializa a contagem de pontos
    jogando = True  # Flag que mantém o jogo rodando
    game_over = False  # Flag que indica se o jogo acabou

    # Lista para acompanhar se o obstáculo foi ultrapassado
    obstaculos_ultrapassados = []

    # Loop principal do jogo
    while jogando:
        gameDisplay.blit(fundo1, (0, 0))  # Desenha o fundo na tela 

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Fecha o jogo quando o evento de fechar a janela ocorre

            if game_over:
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                    game_loop()  # Reinicia o jogo ao pressionar 'R'

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and no_chao:
                    velocidade_y = pulo  # Faz o cubo pular
                    no_chao = False  # Marca que o cubo não está mais no chão
                if evento.key == pygame.K_LEFT:
                    velocidade_x = -velocidade_cubo  # Move o cubo para a esquerda
                if evento.key == pygame.K_RIGHT:
                    velocidade_x = velocidade_cubo  # Move o cubo para a direita
                if evento.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()  # Fecha o jogo quando a tecla espaço for pressionada

            if evento.type == pygame.KEYUP:
                if evento.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    velocidade_x = 0  # Para o movimento horizontal quando a tecla for solta

        if not game_over:
            # Aplica a gravidade no cubo
            velocidade_y += gravidade
            cubo_y += velocidade_y

            # Movimenta o cubo horizontalmente
            cubo_x += velocidade_x

            # Impede que o cubo saia da tela
            cubo_x = max(0, min(cubo_x, largura_da_tela - cubo_largura))

            # Impede que o cubo caia abaixo do chão
            if cubo_y >= chao_y - cubo_altura:
                cubo_y = chao_y - cubo_altura
                no_chao = True  # Marca que o cubo está no chão
                velocidade_y = 0  # Zera a velocidade no eixo Y

            # Gera obstáculos periodicamente
            contador_obstaculo += 1
            if contador_obstaculo >= tempo_entre_obstaculos:
                contador_obstaculo = 0  # Reseta o contador
                tipo = random.choice(["cima", "direita"])  # Sorteia o tipo de obstáculo

                # Obstáculo que cai do topo da tela
                if tipo == "cima":
                    obstaculo = pygame.Rect(random.randint(0, largura_da_tela - 40), 0, 40, 40)
                else:  # Obstáculo vindo da direita
                    obstaculo = pygame.Rect(largura_da_tela, chao_y - 40, 40, 40)

                obstaculos.append(obstaculo)  # Adiciona o obstáculo à lista

            # Move os obstáculos
            for obstaculo in obstaculos:
                if obstaculo.y == 0:  # Se o obstáculo estiver no topo
                    obstaculo.y += 350  # Faz com que ele desça até a posição 300 no eixo Y
                else:
                    obstaculo.x -= 5  # Faz o obstáculo se mover da direita para a esquerda

            # Verifica colisão com obstáculos
            for obstaculo in obstaculos:
                if pygame.Rect(cubo_x, cubo_y, cubo_largura, cubo_altura).colliderect(obstaculo):
                    game_over = True  # Se houver colisão, o jogo termina
                else:
                    # Checa se o cubo ultrapassou o obstáculo no eixo X
                    if cubo_x + cubo_largura > obstaculo.x and obstaculo not in obstaculos_ultrapassados:
                        obstaculos_ultrapassados.append(obstaculo)  # Marca o obstáculo como ultrapassado
                        pontos += 1  # Só soma pontos quando o cubo ultrapassa o obstáculo

            # Exibe o placar na tela
            texto_placar = exibe_mensagem(f'Pontos: {pontos}', 40, (255, 255, 255))
            gameDisplay.blit(texto_placar, (520, 30))

        # Desenha o chão e o teto
        pygame.draw.rect(gameDisplay, cor_do_chao, (0, chao_y, largura_da_tela, base))
        pygame.draw.rect(gameDisplay, cor_do_teto, (0, 0, largura_da_tela, teto_altura))

        # Desenha o cubo e os obstáculos
        pygame.draw.rect(gameDisplay, cor_do_cubo, (cubo_x, cubo_y, cubo_largura, cubo_altura))
        for obstaculo in obstaculos:
            pygame.draw.rect(gameDisplay, cor_obstaculo, obstaculo)

        # Se o jogador perdeu, exibe a mensagem de "Game Over"
        if game_over:
            texto_game_over = fonte.render("Acho que perdeu!", True, (255, 0, 0))
            gameDisplay.blit(texto_game_over, (largura_da_tela // 4, altura_da_tela // 2))
            texto_reiniciar = fonte.render("Pressione R para reiniciar", True, (255, 255, 255))
            gameDisplay.blit(texto_reiniciar, (largura_da_tela // 4, altura_da_tela // 2 + 50))
            texto_sair = fonte.render("Caso queira desistir, aperte a tecla Espaço", True, (255, 255, 255))
            gameDisplay.blit(texto_sair, (largura_da_tela // 4, altura_da_tela // 2 + 100))

        pygame.display.update()  # Atualiza a tela com as novas informações

        clock.tick(60)  # Controla a taxa de quadros (FPS) do jogo

# Exibir instruções
exibir_instrucoes()

# Rodar o jogo
game_loop()
pygame.quit()  # Encerra o pygame
