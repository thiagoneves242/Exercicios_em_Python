"""
Faça um programa que leia um valor N inteiro e positivo,
calcule o mostre o valor E, conforme a fórmula a seguir
E = (1 + 1) / 1! + (1 /2!) + (1/3!)+....+1/N!
"""
n = int(input("= "))
i, fat_n, e = 1, 1, 1.0
while i <= n:
    fat_n = fat_n * i
    print("fatorial", fat_n)
    e += 1 / fat_n
    print(e)
    i += 1
