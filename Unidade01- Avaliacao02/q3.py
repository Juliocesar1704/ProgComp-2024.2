# Codigo feito por Júlio César e David Douglas

primeiro_primo = 3
# Declaramos aqui qual o primeiro número primo e onde devemos começar
limite = 1000000
# Aqui declaramos o teto de onde podemos chegar
pares_de_primos = 0
# Aqui declaramos a variável que vai contar a quantidade de pares de números primos
qtdPrimos = 0
# Aqui declaramos a variável que vai contar a quantidade de números primos
ultPrimo = 0
# Aqui declaramos a variável que vai guardar o último número primo encontrado

for num in range(primeiro_primo, limite + 1, 2):
    div = 1
    ndiv = 0
    # Aqui verificamos se o número é primo 
    while div <= num:
        if num % div == 0:
            ndiv += 1
        div += 1
    
    # Se o número de divisões for igual a 2, o número é primo
    if ndiv == 2:
        qtdPrimos += 1
        # Verificamos se os últimos dois primos ímpares encontrados são consecutivos
        if ultPrimo != 0 and num - ultPrimo == 2:
            # Se forem consecutivos, ele adiciona o contador que será usado para mostrar a quantidade de pares
            pares_de_primos += 1
        ultPrimo = num

print(f"A quantidade de pares de números primos consecutivos entre 3 e 1000000 é: {pares_de_primos}")

"""
Ideias para melhorar o código:

# Peidr para o usuário digitar o o inicio e o fim do intervalo
primeiro_primo = int(input("Digite o primeiro número primo: "))
limite = int(input("Digite o limite: "))

# Adicionar uma lista para armazenar os números primos encontrados e exibilos no final

# Adicionando a quantidade total de números primos encontrados
print(f"A quantidade total de números primos entre 3 e 1000000 é: {qtdPrimos}")

"""
