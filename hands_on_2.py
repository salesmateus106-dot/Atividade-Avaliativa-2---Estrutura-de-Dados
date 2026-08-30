import random

# Solicitar ao usuário o limite de temperatura
limite = float(input("Digite o limite de temperatura para verificação (°C): "))

# Criando a matriz 5x24
sensores = [[0.0] * 24 for _ in range(5)]

# Preenchimento automático com temperaturas aleatórias (18.0 °C a 35.0 °C)
for i in range(5):
    for j in range(24):
        sensores[i][j] = round(random.uniform(18.0, 35.0), 1)

# Inicialização de variáveis
maior_temp = sensores[0][0]
sensor_maior = 0
horario_maior = 0
soma_geral = 0
acima_limite = 0
media_sensor = [0.0] * 5

# Processamento dos dados da matriz
for i in range(5):
    soma_sensor = 0
    for j in range(24):
        temp = sensores[i][j]
        soma_sensor += temp
        soma_geral += temp

        # 2, 3 e 4. Verifica a maior temperatura e guarda suas posições
        if temp > maior_temp:
            maior_temp = temp
            sensor_maior = i
            horario_maior = j

        #  Contagem de leituras acima do limite estipulado
        if temp > limite:
            acima_limite += 1

    #  Média das 24 medições de cada sensor
    media_sensor[i] = soma_sensor / 24

# Média geral das 120 medições (5 * 24)
media_geral = soma_geral / (5 * 24)

# Exibição dos resultados organizados
print("\n" + "="*40)
print("       RELATÓRIO DE TEMPERATURAS")
print("="*40)

#  Exibe a média individual de cada sensor
for i in range(5):
    print(f"Média do Sensor {i+1}: {media_sensor[i]:.2f} °C")

print("-" * 40)
# 2, 3, 4, 5 e 6. Resultados estatísticos finais
print(f"Média geral: {media_geral:.2f} °C")
print(f"Maior temperatura: {maior_temp:.2f} °C")
print(f"Sensor responsável: {sensor_maior}")
print(f"Horário da ocorrência: {horario_maior}h")
print(f"Leituras acima do limite ({limite:.1f} °C): {acima_limite}")
print("="*40)


"""
1. Por que são necessários loops aninhados

A matriz possui duas dimensões: linhas (sensores) e colunas (horários). Um único loop só consegue andar em uma direção por vez (como uma linha reta). Para percorrer uma tabela completa, usamos um loop externo para fixar a linha atual (ex: Sensor 0) e um loop interno para passar por todas as colunas daquela linha (Horários 0 a 23). Quando o loop interno termina, o externo avança para a próxima linha e o processo se repete.

2. O papel dos índices [i][j]

Os índices funcionam como as coordenadas de um mapa ou batalha naval para localizar um valor exato dentro da matriz:

i (Linha): Representa qual sensor está sendo acessado (de 0 a 4).

j (Coluna): Representa qual horário do dia está sendo acessado (de 0 a 23).

sensores[i][j]: É o valor da temperatura armazenado exatamente no cruzamento do Sensor i na Hora j.

3. Quantas posições da matriz são percorridas

São percorridas 120 posições.

Cálculo: $5 \text{ linhas (sensores)} \times 24 \text{ colunas (horas)} = 120 \text{ posições}$.

4. Relação entre linhas, colunas e quantidade de operações

A quantidade total de repetições e operações do programa é diretamente proporcional ao produto entre o número de linhas ($L$) e o número de colunas ($C$).

Fórmula do Total de Operações: $\text{Operações} = L \times C$

Se você tiver 5 sensores e 24 horas, o loop interno roda $5 \times 24 = 120$ vezes.

Se você dobrar para 10 sensores e manter 24 horas, as operações dobram para $10 \times 24 = 240$ vezes.

"""