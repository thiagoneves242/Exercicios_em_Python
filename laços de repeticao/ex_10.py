"""
faça um algorítimo que calcule e mostre a soma dos 50 primeiros números pares
"""
soma: int = 0
for i in range(0, 101, 2):
    """if i % 2 == 0:"""
    soma = soma + i
print('Primeira forma: {}'.format(soma))

"""segunda forma"""
soma: int = 0
i: int = 0
while i <= 100:
    if i % 2 == 0:
        soma = soma + i
        soma = soma
    i = i + 1
print('Segunda forma: {}'.format(soma))
