"""
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido.
A quantidade de números a serem lidos deve ser fornecida pelo usuario.
"""
qtd_num = int(input())
cont = {}
maior, i = 0, 0

for i in range(i, qtd_num):
    num = (int(input("digite o numero= ")))
    if num > maior:
        maior = num
    c = cont.get(num, 0)
    cont[num] = c + 1
print(f'O maior valor é {maior} e ele ocorre {cont[maior]} vez(es)')
