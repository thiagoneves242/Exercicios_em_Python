"""
faça um program que leia um numero inteiro positivo impar n e imprima
todos os números de 1 até N em ordem crescente
"""
n = int(input())
if 0 < n % 2 > 0:
    impar: int = 1
    i: int = 0
    while i < n:
        print(f"primeira forma impares {impar}")
        impar += 2
        i += 2

"""***********"""
n = int(input())
if n % 2 != 0 or n > 0:
    impar: int = 1
    for i in range(0, n, 2):
        print(f"segunda forma impares {impar}")
        impar = impar + 2
