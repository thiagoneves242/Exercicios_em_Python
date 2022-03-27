"""
Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número,
com exceção dele próprio ex: a soma dos divisores do número 66 é 1 + 2 + 3 + 11 + 22 + 33 = 78
"""
n = int(input("= "))
divisor = 0
soma_divisor = 0

while divisor < n - 1:
    divisor += 1
    if n % divisor == 0:
        print(divisor)
        soma_divisor += divisor
print(soma_divisor)
