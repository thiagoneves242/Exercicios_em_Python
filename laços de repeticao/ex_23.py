"""
faça um algorítimo que leia um número positivo e imprima seus divisores
"""
n = int(input("= "))
divisor = 0
while divisor <= n:
    divisor += 1
    if n % divisor == 0:
        print(divisor)

"""
segunda forma 
"""
print("segunda forma")
n2 = int(input("= "))
divisor2 = 0
for i in range(0, n2):
    divisor2 += 1
    if n2 % divisor2 == 0:
        print(divisor2)
