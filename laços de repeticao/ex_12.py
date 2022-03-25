"""
faça um programa que leia um numero inteiro positivo N
e imprima todos os numeros naturais de 0 até N em ordem decrescente
"""
n = int(input())
i = n + 1
if n % 2 == 0:
    while i > 0:
        i = i - 1
        print(f'Primeira forma: {i}')
"""***********"""
n = int(input())
i = 0
if n % 2 == 0:
    for i in range(n, -1, -1):
        print(f'segunda forma {i}')