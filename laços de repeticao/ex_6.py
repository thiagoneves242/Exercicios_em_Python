"""
faça um algorítimo que leia 10 valores inteiros e imprimima sua media
"""
soma: int = 0
media: float = 0
for i in range(0, 10):
    n = int(input())
    soma += n
    media = soma / 10
print(f"primeira forma, meida: {media}")

"""************"""
soma: int = 0
valor: int = 0
i = 0
while i < 10:
    n = int(input())
    soma += n
    media = soma / 10
    i = i + 1
print(f"segunda forma, meida: {media}")
