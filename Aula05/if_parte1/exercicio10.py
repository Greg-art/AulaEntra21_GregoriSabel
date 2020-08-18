# Exercicio 10
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem decrescente.
# 

n1 = int(input("Diga um numero: "))
n2 = int(input("diga outro numero: "))
n3 = int(input("diga um terceiro numero: "))


if (n1 < n2): # n1<n2
    if(n2<n3):# n1<n2<n3
        print(str(n3)+" "+str(n2)+" "+ str(n1))
    elif(n1<n3): # n1<n3<n2
        print(str(n2)+" "+str(n3)+" "+ str(n1))
    else:# n3<n1<n2
        print(str(n2)+" "+str(n1)+" "+ str(n3))
else: # n2<n1
    if(n3<n2): # n3<n2<n1
        print(str(n1)+" "+str(n2)+" "+ str(n3))
    elif(n3<n1): # n2<n3<n1  
        print(str(n1)+" "+str(n3)+" "+ str(n2))
    else: #n2<n1<n3 
        print(str(n3)+" "+str(n1)+" "+ str(n2))