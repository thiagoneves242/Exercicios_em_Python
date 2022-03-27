"""
faça um algorítimo que leia um número positivo e imprima seus divisores
"""
n = int(input("= "))
divisor = 0
while divisor <= n:
    divisor += 1
    if n % divisor == 0:
        print(divisor)

