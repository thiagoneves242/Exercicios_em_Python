"""
faça um algoritimo que leia um numero inteiro positivo par N
e imprima todos os numeros pares de 0 ate N em ordem decrescente
"""
n = int(input())
i = 0
if n % 2 == 0:
    while i <= n:
        if i % 2 == 0:
            print('Prima forma: {}'.format(i))
        i = i + 1
"""*************"""
n = int(input())
i = 0
if n % 2 == 0:
    for i in range(0, n + 1, 2):
        print('segunda forma: {}'.format(i))