"""
faça um algorítimo que receba dois números. calcule e mostre:
. a soma dos números pares desse intervalo de números, incluindo os números digitados
.a multiplicação os números ímpares desse intervalo, incluindo os digitados
"""
par = 0
impar = 1
num_1, num_2 = input("informe dois valores separados por espaço: ").split()
num_1 = int(num_1)
num_2 = int(num_2)

if num_1 >= num_2:
    maior = num_1
    menor = num_1
else:
    maior = num_2 
    menor = num_1
for i in range(menor, maior + 1):
    if i % 2 == 0:
        par += i
    if i % 2 > 0:
        impar *= i
print(f"A soma dos números pares nesse intervalo é {par}")
print(f"A multiplicação dos números impares nesse intervalo é {impar}")
