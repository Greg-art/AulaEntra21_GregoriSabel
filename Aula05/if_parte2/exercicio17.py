# Exercicio 17
# crie um programa que peça 4 notas de um aluno e calcule a média "(nota1+nota2+nota3+nota4)/4" e retorne:
# 
# Pra média igual a 10 apareça a mensagem "Aprovado com louvor"
# Pra média maior igual a 7 apareça a mensagem "Aprovado"
# Pra média menor que 7 apareça a mensagem "Reprovado"

soma = 0

for i in "1234":
    nota = int(input("Diga sua nota: "))
    soma += nota

media = soma/4

if(media>= 7):
    print("Aprovado" if media<10 else "Aprovado com louvor")
else:
    print("Reprovado!")