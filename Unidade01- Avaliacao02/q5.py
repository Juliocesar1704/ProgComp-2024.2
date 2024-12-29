import datetime

# Data inicial
ano_inicial = 1968
mes_inicial = 4
dia_inicial = 27

# Obtendo a data atual
hoje = datetime.date.today()
ano_hoje, mes_hoje, dia_hoje = hoje.year, hoje.month, hoje.day

# Contando anos bissextos manualmente
anos_bissextos = 0
for ano in range(ano_inicial, ano_hoje + 1):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        anos_bissextos += 1

# 
dias_no_ano_inicial = (12 - mes_inicial) * 30 + (30 - dia_inicial)

# 
dias_no_ano_atual = (mes_hoje - 1) * 30 + dia_hoje

# 
anos_completos = ano_hoje - ano_inicial - 1
dias_anos_intermediarios = anos_completos * 365


dias_totais = dias_no_ano_inicial + dias_no_ano_atual + dias_anos_intermediarios + anos_bissextos

# Contabilizando os sábados
# O dia 27 de abril de 1968 é um sábado (dia 5 na semana) determinado pela questão
sabados_contados = 0
for dia in range(dias_totais + 1):
    if (dia + 5) % 7 == 0:
        sabados_contados += 1


dia_da_semana = hoje.strftime('%A, %d %B %Y')

# Exibindo os resultados
print(f"Data inicial: {ano_inicial}-{mes_inicial}-{dia_inicial}")
print(f"Desde {ano_inicial}{mes_inicial}{dia_inicial}, na presente data {hoje}, fazem cerca de {dias_totais} dias")
print("Hoje é:", dia_da_semana)
print(f"Se passaram {sabados_contados} sábados até a presente data.")
