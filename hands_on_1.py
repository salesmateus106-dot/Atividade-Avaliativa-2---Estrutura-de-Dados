import random


limite = 28.0


sensores = [[0.0] * 24 for _ in range(5)]

for i in range(5):
    for j in range(24):
        # Gera valores aleatórios com 1 casa decimal
        sensores[i][j] = round(random.uniform(18.0, 35.0), 1)

# Inicializações
maior_temp = sensores[0][0]
sensor_maior = 0
horario_maior = 0
soma_geral = 0
acima_limite = 0
media_sensor = [0.0] * 5

# Processamento dos dados
for i in range(5):
    soma_sensor = 0
    for j in range(24):
        temp = sensores[i][j]
        soma_sensor += temp
        soma_geral += temp
       
        if temp > maior_temp:
            maior_temp = temp
            sensor_maior = i
            horario_maior = j
           
        if temp > limite:
            acima_limite += 1
           
    media_sensor[i] = soma_sensor / 24

# Cálculos finais
media_geral = soma_geral / (5 * 24)

# Saída dos resultados
print(f"Média geral: {media_geral:.2f} °C")
print(f"Maior temperatura: {maior_temp:.2f} °C")
print(f"Sensor: {sensor_maior}")
print(f"Horário: {horario_maior}")
print(f"Acima do limite ({limite} °C): {acima_limite} leituras")

"""

No algoritmo são necessárias 3 operações de percurso no array, onde elas foram:
1. Cadastro e processamento inicial das temperaturas. Linhas 14 a 26
2. Mostrando elementos. Linhas 30 e 31
3. Contagem de elementos acima da média. Linhas 36 a 38

Por o array está fixo em ter no máximo 10 temperaturas sua complexidade pode ser considerada como O(1) por sempre ter que percorrer o mesmo número de elementos. Porém se retirar essa limite do código o array passa a ter uma complexidade de O(n) por ter um crescimento linear a depender de quantas variáveis são inseridas nela

"""