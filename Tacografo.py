# Tacógrafos são dispositivos instalados em determinados tipos de veículos, que registram a velocidade, tempo e distância percorrida por tal veículo. É utilizada principalmente em veículos de transporte coletivo e de transporte de cargas, assim ajudando a evitar abusos de velocidade por parte dos motoristas.
# A empresa SBC (Sociedade Brasileira dos Caminhoneiros) decidiu encomendar uma versão um pouco mais básica (e barata) para seus associados não precisarem gastar tanto na instalação desses aparelhos. Essas versões modificadas registram apenas os intervalos de tempo e as velocidades médias do caminhão naqueles intervalos.
# Apesar das restrições dos aparelhos novos, a SBC quer poder saber qual foi a distância percorrida pelos caminhões. Você deverá escrever um programa que recebe uma série de intervalos de tempo com suas respectivas velocidades médias e calcula qual foi a distância total percorrida pelo caminhão de acordo com o tacógrafo.

# Entrada:
# A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 1000) representando a quantidade de intervalos de tempo registrados no tacógrafo. As N linhas seguintes descrevem os intervalos de tempo. Cada uma dessas linhas possui dois inteiros T e V (1 ≤ T ≤ 100, 0 ≤ V ≤ 120), que representam, respectivamente o tempo decorrido (em horas) e a velocidade média (em quilômetros por hora) no intervalo de tempo.

# Saída:
# Seu programa deve imprimir uma única linha, contendo um único número inteiro representando a distância total percorrida, em quilômetros.

# Exemplos de Entrada:
# 1:
#   3
#   10 0
#   55 12
#   75 120

# 2:
#   10
#   45 46
#   46 101
#   7 2
#   95 104
#   12 107
#   78 29
#   10 26
#   52 86
#   13 79
#   1 107

# 3:
#   8
#   37 24
#   68 69
#   28 26
#   79 8
#   36 0
#   50 71
#   13 68
#   87 113


# Exemplos de Saída:
# 1: 9660
# 2: 26022
# 3: 21205

# Status: (Accepted)

nums = int(input(""))
intervals = []
count = 0

for n in range(0, nums):
    intervals.append(input(""))

for interval in intervals:
    t, v = interval.split(" ")
    count += int(t) * int(v)

print(count)
