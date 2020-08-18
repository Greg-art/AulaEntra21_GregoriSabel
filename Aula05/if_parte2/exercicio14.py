# Exercicio 14
# Crie um programa que peça ao usuário digitar um número de 1 a 7 e mostre o dia da semana correspondente sendo que segunda feira é o
# numero 1 e domingo é 7.

dia = int(input("escolha o dia da semana pelo seu respectivo numero: "))

print("")

if (dia == 1):
    print("Segunda-feira")
elif(dia == 2):
    print("Terça-feira")
elif(dia == 3):
    print("Quarta-feira")
elif(dia == 4):
    print("Quinta-feira")
elif(dia == 5):
    print("Sexta-feira")
elif(dia == 6):
    print("Sabado")
elif(dia == 7):
    print("Domingo")
else:
    print("Escolha um numero válido por favor")