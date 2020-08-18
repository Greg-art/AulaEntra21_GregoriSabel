# Exercicio 7
# Faça um programa que peça 3 números inteiros e mostre o menor número.


n1 = int(input("Diga um numero: "))
n2 = int(input("diga outro numero: "))
n3 = int(input("diga um terceiro numero: "))


if (n1 < n2 and n1 < n3):
    print("o numero "+str(n1)+" é o menor")
elif (n2 < n1 and n2 < n3):
    print("o numero "+str(n2)+" é o menor")
else:    
    print("o numero "+str(n3)+" é o menor")



