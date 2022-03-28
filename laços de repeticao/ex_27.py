"""
Em Matemática um número harmônico designado por H(n) define-se como sendo a soma da série harmônica:
H(n) = (1 + 1) / 2 + (1/3) + (1/4) +....+1/n
faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n)
"""
n = int(input("= "))
i, soma, = 1, 0
while i <= n:
    soma += 1 / i
    i += 1
print(f"a soma do valor harmônico de N é= {soma}")

"""
segunda forma 
"""
print("segunda forma")
v = int(input("= "))
soma2 = 0
for i in range(1, v + 1):
    soma2 += 1 / i
print(f"a soma do valor harmônico de N é= {soma2}")

