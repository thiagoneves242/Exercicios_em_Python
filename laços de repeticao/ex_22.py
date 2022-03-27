"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado.
Uma sequência de notas (válidas no intervalo de 10 a 20)e que mostre na tela como resultado,
a correspondente média aritmética.
O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido ao programa,
o qual terminará quando for introduzido um valor que não seja válido como nota de aprovação.
"""

soma, media, cont = 0, 0, 0
while True:
    notas = int(input("nota= "))
    if 10 <= notas <= 20:
        soma += notas
        cont += 1
        media = int(soma / cont)
    else:
        break
print(f"Media={media}")

"""
segunda forma 
"""
print("segunda forma")
soma2, media2, cont2 = 0, 0, 0,
notas2 = 0
for i in range(0, 1000):
    notas2 = int(input("notas= "))
    if 10 <= notas2 <= 20:
        soma2 += notas2
        cont2 += 1
        media2 = int(soma2 / cont2)
    else:
        break
print(f"Media={media2}")
