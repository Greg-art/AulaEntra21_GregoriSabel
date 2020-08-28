"""Exercicio 05

Faça um programa que peça ao usuário digitar a quantidade de vendas do dia. Cadastre cada venda separadaemnte e depois mostre a média e o valor total vendido no dia.
"""
qtd = int(input("quantas vendas?"))
total = 0

for i in range(qtd):
    grana = int(input("quanto foi"))
    total += grana

print("\nO total foi: " + str(total))
print("\nA media foi: " + str(total / qtd))