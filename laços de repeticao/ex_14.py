"""
faça um algoritimo que leia um numero inteiro positivo par N
e imprima todos os numeros pares de 0 ate N em ordem decrescente
"""
n = int(input())
i = n

if n % 2 == 0:
    while i >= 0:
        if i % 2 == 0:
            print('primeira forma {}'.format(i))
        i = i - 1

"""*********************"""
n = int(input())
i = n
if n % 2 == 0:
    for i in range(n, -1, -1):
        if i % 2 == 0:
            print('Segunda forma {}'.format(i))
