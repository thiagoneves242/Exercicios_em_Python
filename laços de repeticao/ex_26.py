"""
faça um algorítimo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado
"""
n = int(input("= "))
cont, mult_11, mult_13, mult_17 = 1, 11, 13, 17
while cont < n:
    if cont % n == mult_11 or cont % mult_13 == 0 or cont % mult_17 == 0:
        print(cont)
        break
    cont += 1

"""
segunda forma 
"""
print("segunda forma")
n1 = int(input("= "))
i = 1
for i in range(i, n):
    if i % 11 == 0 or i % 13 == 0 or i % 17 == 0:
        print(i)
        break
