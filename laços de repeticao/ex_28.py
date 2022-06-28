"""
Faça um programa que leia um valor N inteiro e positivo,
calcule o mostre o valor E, conforme a fórmula a seguir
E = (1 + 1) / 1! + (1 /2!) + (1/3!)+....+1/N!
"""
n = int(input("= "))
i, j = 1, 1
e = 1.0
fat = float
for i in range(i, n):
    fat = 1
    for j in range(j, i):
        fat = fat * j
        j += 1
    e = e + 1.0 / fat
    print(e)
    i += 1

