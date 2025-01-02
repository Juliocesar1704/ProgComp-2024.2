import random

# Configuração de cores
reset_cor = '\033[0;0m'  # Retoma a cor padrão
letra_inexiste = '\033[40m'     # Fundo preto
letra_pos_errado = '\033[43m'   # Fundo amarelo
letra_pos_correta = '\033[42m'  # Fundo verde

# Lista de palavras possíveis
termo = ("ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA")

# Palavras sorteadas
sorteada_1 = random.choice(termo)
sorteada_2 = random.choice(termo)
fim_do_jogo = False
chances = 7

# Instruções
print("Dicas do jogo")
print("Você deve escolher duas palavras com até 5 letras cada.")
print(letra_pos_correta + "T" + reset_cor + "ERNO -> a letra 'T' faz parte da palavra e está na posição correta")
print("VA" + letra_pos_errado + "L" + reset_cor + "SA -> a letra 'L' faz parte da palavra, mas em outra posição")
print("PUL" + letra_inexiste + "G" + reset_cor + "A -> a letra 'G' não faz parte da palavra")
print("------------------------------------------------------------------------------------")

# Loop principal
while not fim_do_jogo:
    tela_1, tela_2 = [], []
    chute1 = input("Digite a primeira palavra (5 letras): ").upper()[:5]
    chute2 = input("Digite a segunda palavra (5 letras): ").upper()[:5]
    chances -= 1

    # Verificação de vitória
    if chute1 == sorteada_1 and chute2 == sorteada_2:
        print(f"Parabéns, você acertou as duas palavras! ({sorteada_1} e {sorteada_2})")
        fim_do_jogo = True
    elif chances == 0:
        print(f"Acabaram as chances. As palavras eram {sorteada_1} e {sorteada_2}.")
        fim_do_jogo = True
    else:
        # Verificação da palavra 1
        i = 0
        for c in chute1:
            if c in sorteada_1:
                if c == sorteada_1[i]:
                    tela_1.append(letra_pos_correta + c + reset_cor)
                else:
                    tela_1.append(letra_pos_errado + c + reset_cor)
            else:
                tela_1.append(letra_inexiste + c + reset_cor)
            i += 1

        # Verificação da palavra 2
        i = 0
        for c in chute2:
            if c in sorteada_2:
                if c == sorteada_2[i]:
                    tela_2.append(letra_pos_correta + c + reset_cor)
                else:
                    tela_2.append(letra_pos_errado + c + reset_cor)
            else:
                tela_2.append(letra_inexiste + c + reset_cor)
            i += 1

        # Exibição dos resultados
        print("Palavra 1:", ''.join(tela_1))
        print("Palavra 2:", ''.join(tela_2))
