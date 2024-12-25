contadorP = 0 
# Aqui declaramos a variavel que vai contar a quantidade de palindromos

for pos in range(10, 10000 + 1): 
    # Procura os números palindromos entre 10 e 100000
    num = pos 
    # Recebe e guarda o numero
    numR = 0 
    # Aqui declaramos a variavel que recebe o numero de forma inversa

    while pos > 0: 
    # Aqui criamos a repetição para inverter o numero
        ultimo_digito = pos % 10 
        # Aqui a variavel recebe e guarda o último dígito
        numR = numR * 10 + ultimo_digito 
        # Aqui faz a inverção do numero
        pos = pos // 10 
        # Aqui retira o último dígito

    if num == numR:
        # verifica se o número e o numero inverso são iguais se forem o numero é palindromo
        contadorP += 1 
        # adiciona 1 ao contador

print(f"A quantidade de numeros palindromos entre 10 e 10000 é : {contadorP}")
# Aqui exibimos a quantidae de palindromos entre 10 e 10000
