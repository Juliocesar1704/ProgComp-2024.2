# Codigo feito por Júlio César e David Douglas

import datetime

# Data inicial.
ano_inicial = 1968
mes_inicial = 4
dia_inicial = 27

# Obtendo a data atual e formatando para normas brasileira de exibição que será Dia/Mes/Ano.
hoje = datetime.date.today()
hoje_formato_BR = hoje.strftime('%d/%m/%Y')
ano_hoje, mes_hoje, dia_hoje = hoje.year, hoje.month, hoje.day

# Contando anos bissextos manualmente.
anos_bissextos = 0
for ano in range(ano_inicial, ano_hoje + 1):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        anos_bissextos += 1

# Ele fará as contagens do dias partindo da data primária que a questão determinou até o dia atual. 
dias_no_ano_inicial = (12 - mes_inicial) * 30 + (30 - dia_inicial)
dias_no_ano_atual = (mes_hoje - 1) * 30 + dia_hoje
anos_completos = ano_hoje - ano_inicial - 1
dias_anos_intermediarios = anos_completos * 365

dias_totais = dias_no_ano_inicial + dias_no_ano_atual + dias_anos_intermediarios + anos_bissextos

# Contabilizando os sábados.
# O dia 27 de abril de 1968 é um sábado (dia 5 na semana) determinado pela questão.
sabados_contados = 0
for dia in range(dias_totais + 1):
    if (dia + 5) % 7 == 0:
        sabados_contados += 1

# Apenas uma questão estética ele não interfere no código, apenas mostra por extenso a data.
# Tentamos utilizar para PT.BR porém deu erro.
dia_da_semana = hoje.strftime('%A, %d de %B de %Y')

# Exibindo os resultados.
print(f"Data inicial: {dia_inicial}/{mes_inicial}/{ano_inicial}")
print(f"Desde {dia_inicial}/{mes_inicial}/{ano_inicial}, na presente data {hoje_formato_BR}, fazem cerca de {dias_totais} dias")
print(f"Hoje é {dia_da_semana}")
print(f"Se passaram {sabados_contados} sábados até a presente data.")
