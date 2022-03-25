"""
faça um programa que leia um número inteiro positivo N
e imprima todos os números naturais de 0 até N em ordem crescente
"""
n = int(input())
for i in range(0, n + 1):
    print(f'Pimeira forma: {i}')
"""************"""
n = int(input())
i = 0
while i <= n:
    print(f'Segunda forma: {i}')
    i = i + 1
