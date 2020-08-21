"""Execicios 02

Escreva um programa que receba 4 notas e calcule a média.
Mostre a seguinte mensagem conforme a media final.

Media Final
de 0 a 5 - Reprovado
de 5 a 6.5 - Recuperação
de 6.5 a 9 - Aprovado
Acima de 9 - Aprovado com louvor
"""

total = 0
for i in [1,2,3,4]:
    nota = float(input("diga sua"+str(i)+"º nota"))
    total += nota

media = total/4

if (media > 0 and media <= 5):
    resposta = "Reprovado"
elif (media > 5 and media <= 6.5):
    resposta = "Recuperação"
elif (media > 6.5 and media <= 9):
    resposta = "Aprovado"
else:
    resposta = "Aprovado com louvor"
print(resposta)