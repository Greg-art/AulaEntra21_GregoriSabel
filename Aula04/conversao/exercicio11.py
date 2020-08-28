# Exercicio 11
# Escreva um programa que peça o peso (float) de 3 pessoas e motre na tela a soma de todos os pesos. 

amount = int(input("De quantas pessoas você deseja calcular a soma dos pesos"))
total = 0

for x in range(amount):
    peso = float(input("peso da "+ str(x+1) +"º pessoa: "))
    total = total + peso

print("A soma do peso das três pessoas é: "+ str(total) +" quilos")





