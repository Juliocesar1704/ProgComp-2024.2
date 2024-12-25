# Estaremos utilizando de uma biblioteca para usar das funções determinadas no enunciado da questão
import datetime
# Poderiamos trocar a data inicial para uma váriavel onde o abençoado que fosse testar o código iria digitar um data
# Com isto o código apresentaria mais algumas váriaveis afim de evitar que seja informado dados divergente do que o código está preposto a fazer
data_inicial = datetime.date(1968, 4, 27)
hoje = datetime.date.today()
contador = (hoje - data_inicial).days
#Essa função é só por estética para informar o dia da semana não interfere no código
dia_da_semana = hoje.strftime('%A, %d %B %Y')
dia_inicial = 0
# Partindo desda parte do código começaremos a contabilizar o sabádos que é o dia 5 da semana 5 na linguagem onde começa em 0 
# Segunda = 0, Terça = 1, Quarta = 2, Quinta = 3, sexta = 4 e o sabado = 5
# A divisão por 7 para localizar os dias que serão o quinto = sabádo seguindo a lógica acima citada
dia_de_sabado = 5
for dia in range ( contador + 1):
    dia_atual = (dia_inicial + dia) % 7
    if dia_atual == 5:
        dia_de_sabado += 1


print("Data inicial:", data_inicial)
print(f"Desde {data_inicial}, na presente data {hoje}, fazem cerca de {contador} dias")
print("Hoje é:", dia_da_semana)
print (f'Se passou {dia_de_sabado} dias de sabados, até presente data')

#Criação de David Douglas
