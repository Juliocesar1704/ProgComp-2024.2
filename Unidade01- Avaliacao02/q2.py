# Codigo feito por Júlio César e David Douglas


# Declaramos aqui qual o primeiro número primo e onde devemos começar
numN = 10
# Aqui declaramos até onde podemos chegar
limite = 1000000
# Aqui declaramos a variavel que vai contar a quantidade de palindromos
contadorP = 0 

for pos in range(numN, limite + 1): 
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

print(f"A quantidade de numeros palindromos entre 10 e 1000000 é : {contadorP}")
# Aqui exibimos a quantidae de palindromos entre 10 e 1000000

"""
Ideias para melhorar o código:

# Peidr para o usuário digitar o o inicio e o fim do intervalo
numN = int(input("Digite o primeiro número: "))
limite = int(input("Digite o limite: "))

# Adicionar uma lista para armazenar os números palindromos encontrados e exibilos no final

# Adicionar a quantidade total de números palindromos encontrados
print(f"A quantidade total de números palindromos entre 10 e 10000 é: {contadorP}")

# Adicionar uma lista para armazenar os números palindromos encontrados e exibilos no final

"""
