"""
faça um algoritimo que leia 10 valores e some os 10 valores
"""
print('ensira 10 valores:')
soma: int = 0
for i in range(0, 10):
    n = int(input())
    soma += n
print(f"primeira formas, soma dos valores: {soma}")

"""*********************"""
print('\nensira 10 valores:')
soma: int = 0
i = 0
while i < 10:
    n = int(input())
    soma += n
    i = i + 1
print(f"segunda forma, soma dos valores: {soma}")