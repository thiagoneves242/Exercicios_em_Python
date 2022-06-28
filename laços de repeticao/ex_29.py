"""
Escreva um programa para calcular o valo da série, para 5 termos
S = 0  +1/2! +2/4! +3/6!+......
"""
n = 5
s = 0
i = 0
for j in range(1, n + 1):
    i += 2
    s = s + 1 / i
    print(s)
