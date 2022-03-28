"""
ler o uma sequência de números inteiros e determine
se eles são pares ou não. Deverá ser informado o número
de dados lidos e números de pares. O processo
só termina quando for digitado 1000
"""
list_par = []
list_impar = []
dados_lidos = 0
qtd_par: int = 0

while True:
    print("[Digite 1000 a qualquer momento para encerrar ou Digite qualquer número para continuar!]")
    num = int(input("= "))
    dados_lidos = dados_lidos + 1
    if num != 1000:
        if num % 2 == 0:
            qtd_par = qtd_par + 1
            list_par.append(str(num))
        else:
            list_impar.append(str(num))
        continue
    break
print(f"quantidade de números pares digitados= {qtd_par}")
print(f"dados lidos= {dados_lidos - 1}")
print(" e ".join(list_par), "é número(s) par(es)! ")
print(" e ".join(list_impar), " é número(s) impar(es)!")


"""list_impar = [str(i) for i in list_impar]"""
