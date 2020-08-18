# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.

n1 = float(input("digite um numero: "))
n2 = float(input("digite outro numero: "))

print("""
O que deseja fazer com esses numeros?

(1)Somar    (2)Subtrair    (3)Multiplicar     (4)Dividir

""")
chosen = int(input())

if (chosen == 1):
    result = n1 + n2
elif(chosen == 2):
    result = n1 - n2
elif(chosen == 3):
    result = n1 * n2
elif(chosen == 4):
    result = n1 / n2
else:
    result = " Algo de estranho aconteceu, tente denovo! "

print(result)
