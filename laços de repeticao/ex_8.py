""""faça um algoritimo que leia 10 valores e imprima o maior e o menor valor lido"""

print("primeira forma")
n = int(input())
maior_numero = n
menor_numero = n
for i in range(0, 9):
    n = int(input())
    if maior_numero < n and menor_numero < n:
        maior_numero = n

    if n < maior_numero < menor_numero:
        maior_numero = menor_numero

    if n > menor_numero > maior_numero:
        menor_numero = maior_numero

    if n < menor_numero < maior_numero:
        menor_numero = n
print("maior numero: ", maior_numero)
print("menor numero: ", menor_numero)

"""*********************"""
print("\nSegunda forma")
n = int(input())
maior_numero = n
menor_numero = n
i: int = 0
while i < 9:
    n = int(input())
    if maior_numero < n and menor_numero < n:
        maior_numero = n

    if n < maior_numero < menor_numero:
        maior_numero = menor_numero

    if n > menor_numero > maior_numero:
        menor_numero = maior_numero

    if n < menor_numero < maior_numero:
        menor_numero = n
    i = i + 1
print(f"maior numero: {maior_numero}")
print(f"menor numero: {menor_numero}")
