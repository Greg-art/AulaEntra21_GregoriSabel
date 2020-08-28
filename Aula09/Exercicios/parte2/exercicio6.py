
"""Exercicio 06

Faça um programa que peça ao usuário que digite o nome de 10 pessoas. Depois mostre cada nome em linhas separadas.
"""
nomes = []
for i in range(10):
    nomes.append(input("Digite um nome"))

for i in range(10):
    print("\n"+ nomes[i] +"")