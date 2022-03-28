"""
 Escreva um algoritmo que leia um número inteiro
 entre 100 e 999 e imprima na saída cada um dos algarismos que compõe o número
"""
loop = True
while loop:
    num = int(input("Por favor digite um valor valido de 100 á 999= "))
    if 100 <= num <= 999:
        for i, algarismo in enumerate(str(num)):
            print(algarismo)
            loop = False
