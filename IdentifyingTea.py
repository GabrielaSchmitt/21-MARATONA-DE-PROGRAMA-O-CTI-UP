# Blind tea tasting is the skill of identifying a tea by using only your senses of smell and taste.
# As part of the Ideal Challenge of Pure-Tea Consumers (ICPC), a local TV show is organized. During the show, a full teapot is prepared and five contestants are handed a cup of tea each. The participants must smell, taste and assess the sample so as to identify the tea type, which can be: (1) white tea; (2) green tea; (3) black tea; or (4) herbal tea. At the end, the answers are checked to determine the number of correct guesses.
# Given the actual tea type and the answers provided, determine the number of contestants who got the correct answer.

# Input:
# The first line contains an integer T representing the tea type (1 ≤ T ≤ 4). The second line contains five integers A, B, C, D and E, indicating the answer given by each contestant (1 ≤ A, B, C, D, E ≤ 4).

# Output:
# Output a line with an integer representing the number of contestants who got the correct answer.


# Input Samples:
# 1:
#   1
#   1 2 3 2 1

# 2:
#   3
#   4 1 1 2 1


# Output Samples:
# 1:
#   2

# 2:
#   0


# Status: (Accepted)

answer = int(input(""))
guesses = input("")
count = 0

for guess in guesses.split(" "):
    if int(guess) == answer:
        count += 1

print(count)
