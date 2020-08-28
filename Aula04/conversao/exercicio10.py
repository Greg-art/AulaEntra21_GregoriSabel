# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.

class Produto:
    def __init__ (self,name,amount,price):
        self.name = name
        self.amount = amount
        self.price = price

produtos = []

amount = [] 
price = []
name = [""]


x = int(input("bom dia! quantos produtos são?"))

i = 0
while(  i < x ):
    name = input("qual é o "+ str(i+1) +"º produto?")
    amount = input("deseja quantas unidades do "+ str(i+1) +"º produto?")
    price = input("qual o preço do "+ str(i+1) +"º produto?")
    produtos.append(Produto(name,amount,price))
    i = i +1
    print("")

for i in produtos:
    total_price = str(int(i.price) * int(i.amount))
    print("a quantidade de "+ i.amount + " " + i.name + " ao preço de "+ i.price + " reais cada, vai custar " + total_price + " reais")
    

