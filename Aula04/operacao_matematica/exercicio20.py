#  Exercicio 20
# Usando a seguinte fórmula:
# 
# valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo
# 
# Crie um programa que solicite ao usuário o valor do dinheiro emprestado, 
# a taxa de juros em porcentagem e o tempo do empréstimo.
# 
# Mostre na telas o valor do dinheiro emprestado, a taxa de juros em porcentagem, 
# tempo do empréstimo e o valor que deve ser devolvido no final do empréstimo.


dinheiro_emprestado = float(input("De quanto sera o emprestimo? "))
taxa_juros = float(input("Qaul a taxa de juros que deseja? "))
tempo_emprestimo = int(input("Quantos meses deve durar o emprestimo? "))

valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo

print(valor_receber)