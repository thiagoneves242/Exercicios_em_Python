"""
faça um algorítimo que faca contagem regressiva de 10 á 0
"""
i: int = 10
print("primeira forma")
while i >= 0:
    print(i)
    i = i - 1
print("FIM")

"""*************"""
print("segunda forma")
i: int = 10
for i in range(i, -1, -1):
    print(i)
print("FIM")
