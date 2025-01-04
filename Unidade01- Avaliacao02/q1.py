# Codigo feito por Júlio César e David Douglas

# Nesse caso em questão iremos trabalhar com valores estipulados
inicio = 10
fim = 987631

soma_decrescente = 0  # Inicializando a soma

# Utilizamos o for devido o conjunto esta definido que é 10 ate 987631
for num_inicial in range(inicio, fim + 1):
    numero = num_inicial  # guardará os valores e fará a verificação se o valor é decrescente 

    # Capturando os dígitos do número
    a = numero // 1000
    numero %= 1000

    b = numero // 100
    numero %= 100

    c = numero // 10
    numero %= 10

    d = numero  # Último dígito

    # Verificando se é decrescente com 4 digitos
    if a >= b and b >= c and c >= d:
        soma_decrescente += num_inicial  # Somando apenas os números decrescentes no parametro do conjunto

# Exibindo a soma dos números decrescentes
print(f"A quantidade de números decrescente de {inicio} até {fim} é: {soma_decrescente}")

"""
Ideias para melhorar o código:

# Peidr para o usuário digitar o o inicio e o fim do intervalo
inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

# Adicionar uma lista para armazenar os números decrescentes encontrados e exibilos no final

# Adicionando a quantidade total de números decrescentes encontrados
print(f"A quantidade total de números decrescentes entre 10 e 987631 é: {qtdDecrescentes}")

"""
