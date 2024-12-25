#nesse caso em questão iremos trabalhar com valores estipulados
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
print(f"A soma dos números decrescente em  {inicio} até {fim} é: {soma_decrescente}")
