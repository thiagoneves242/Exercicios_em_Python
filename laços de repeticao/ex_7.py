
"""
faça um programa que leia 10 números inteiros positivos e imprima a média
"""
soma: int = 0
media: int = 0
for i in range(0, 10):
    n = int(input())
    if n % 2 == 0:
        soma += n
        media = soma / 10
print("Primeira forma ")
print(f"media: {media}\n")
"""***********"""
soma: int = 0
media: int = 0
i: int = 0
while i < 10:
    n = int(input())
    if n % 2 == 0:
        soma += n
        media = soma / 10
    i = i + 1
print("Segunda forma")
print(f"media: {media}")
