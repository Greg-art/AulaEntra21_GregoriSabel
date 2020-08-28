
# Exercicio 9
# Faça um programa que peça o nome do cliente, a quantidade do produto (inteiro) e o preço (float).
# 
# Mostre o nome do cliente e o valor total da venda.


amont = input("Quantas unidades você gostaria de comprar?")
price = input("Qual é o preço que esta na embalagem mesmo? pois esqueci")

totalPrice = int(amont) * int(price)

print("o preço é "+ str(totalPrice) + " reais")
