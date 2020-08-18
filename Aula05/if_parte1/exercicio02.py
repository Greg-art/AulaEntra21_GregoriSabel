# Exercicio 2
# Faça um programa que peça um número.
# 
# Mostre na tela se este número é negativo ou positivo. (lembrando que números positivos são maiores que zero!)

n1 = int(input("Diga um numero: "))

if (n1 == 0):
    print("o numero "+str(n1)+" é zero")
elif (n1>0):
    print("o numero "+str(n1)+" é positivo")
else: 
    print("o numero "+str(n1)+" é negativo")