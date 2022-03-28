"""
faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5
"""
i, mult_3, mult_5, soma = 0, 3, 5, 0
while i < 1000:
    if i % mult_3 == 0 or i % mult_5 == 0:
        print(i)
        soma += i
    i += 1
print(f"a soma dos números múltiplos de 3 e 5 são = {soma}")

"""
segunda forma 
"""
print("segunda forma")
j, mult3, mult5, soma2 = 0, 3, 5, 0

for j in range(j, 1000):
    if j % mult3 == 0 or j % mult5 == 0:
        print(j)
        soma2 += j
print(f"a soma dos números múltiplos de 3 e 5 são = {soma}")
