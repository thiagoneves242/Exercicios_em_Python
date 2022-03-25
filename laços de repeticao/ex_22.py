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
print(media)
