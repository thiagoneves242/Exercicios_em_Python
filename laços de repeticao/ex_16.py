"""
faça um program que leia um numero inteiro positivo impar n e imprima
todos os números de 1 até N em ordem decrescente
"""
n = int(input())
i = n
impar: int = 0
print("\nprimeira forma")
if n % 2 != 0:
    while i > 0:
        impar = impar + 1
        if impar % 2 != 0:
            print(impar)
        i = i - 1

"""****************"""
print("\nsegunda forma")
n = int(input())
impar: int = 0
if n % 2 != 0:
    for i in range(n, -1, -1):
        impar = impar + 1
        if impar % 2 != 0:
            print(impar)