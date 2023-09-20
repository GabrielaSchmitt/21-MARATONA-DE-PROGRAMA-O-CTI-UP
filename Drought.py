# Due to the continuous drought that happened recently in some regions of Brazil, the Federal Government created an agency to assess the consumption of these regions in order to verify the behavior of the population at the #time of rationing. This agency will take some cities (for sampling) and it will verify the consumption of each of the townspeople and the average consumption per inhabitant of each town.

# Input
# The input contains a number of test's cases. The first line of each case of test contains an integer N (1 ≤ N ≤ 1 * 10 6), indicating the amount of properties. The following N lines contains a pair of values X (1 ≤ X ≤ #10) and Y ( 1 ≤ Y ≤ 200) indicating the number of residents of each property and its total consumption (m3). Surely, no residence consumes more than 200 m3 per month. The input's end is represented by zero.

# Output
# For each case of test you must present the message “Cidade# n:”, where n is the number of the city in the sequence (1, 2, 3, ...), and then you must list in ascending order of consumption, the people's amount followed by #a hyphen and the consumption of these people, rounding the value down. In the third line of output you should present the consumption per person in that town, with two decimal places without rounding, considering the total real consumption. Print a blank line between two consecutives test's cases. There is no blank line at the end of output.

# Input Sample:
# 3
# 3 22
# 2 11
# 3 39
# 5
# 1 25
# 2 20
# 3 31
# 2 40
# 6 70
# 2
# 1 1
# 3 2
# 0

# Output Sample:
# Cidade# 1:
# 2-5 3-7 3-13
# Consumo medio: 9.00 m3.
#
# Cidade# 2:
# 5-10 6-11 2-20 1-25
# Consumo medio: 13.28 m3.
#
# Cidade# 3:
# 3-0 1-1
# Consumo medio: 0.75 m3.
#
# Status : (Time limit exceeded)

import math

index = 0
while True:
    num = int(input())
    if num == 0 or num > 1000000:
        break

    sumR = 0
    sumC = 0
    consumptions = []

    for _ in range(num):
        residents, total = map(int, input().split())

        if residents > 10 or total > 200:
            break

        sumR += residents
        sumC += total
        consumptions.append({"r": residents, "c": math.floor(total/residents)})

    media = sumC / sumR
    consumptions = sorted(consumptions, key=lambda x: x["c"])

    consumption = ""
    for c in consumptions:
        consumption += f"{c['r']}-{c['c']} "

    print(f"Cidade# {index + 1}:")
    print(consumption.strip())
    print(f"Consumo medio: {media:.2f} m3.\n")
    index += 1
