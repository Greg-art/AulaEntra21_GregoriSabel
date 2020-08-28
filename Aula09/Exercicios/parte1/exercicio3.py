
"""Exercicio 03

Faça um programa que peça 10 notas do aluno. Faça a média e mostre as seguintes mensagens:

Para 7 a 10 - Aprovado
Para 5.5 a 7 - Recuperação 
Para menor de 5.5 - Reprovado
"""
total = 0
for i in range(10):
    nota = int(input("digite sua " + str(i+1) + "º nota"))
    total += nota
print("sua média é: "+str(total/i))