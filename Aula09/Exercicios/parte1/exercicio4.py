"""Exercicio 04

Faça um programa de cadastro de pessoas que receba 10 nomes, idades e e-mails e salve cada um em uma lista.

Depois mostre as listas separadamente 
(print (lista) já é o suficiente)
"""
listas = []
x = 3

for i in range(x):
    print("\n" + str(i+1) +"º pessoa:")
    nome = input("digite seu nome: ")
    idade = input("digite sua idade: ")
    email = input("digite seu email: ")
    lista = [nome, idade, email]
    listas.append(lista)
print(" ")

for i in range(x):
    print(listas[i])
