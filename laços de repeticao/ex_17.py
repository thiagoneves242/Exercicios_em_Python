"""
 faça um algorítimo que leia um numero inteiro positivo N e calcule a soma dos n primeiros numeros naturais
"""
n = int(input())
i = 1
soma = 0
if n % 2 == 0:
    while i <= n:
        soma = soma + i
        print(soma)
        i = i + 1
    print(f"a soma dos {n} primeiros numeros são: {soma}")
