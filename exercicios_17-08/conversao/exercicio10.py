# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.


x = int(input("bom dia! quantos produtos são?"))


amount = [] 
price = []
product = [""]

i = 0
while(  i < x ):
    product.append(input("qual é o "+ str(i+1) +"º produto?"))
    amount.append(int(input("deseja quantas unidades do "+ str(i+1) +"º produto?")))
    price.append(int(input("qual o preço do "+ str(i+1) +"º produto?")))
    i = i +1
    print("")


i = 0
while(  i < x ):
    total_price = amount[i] * price[i]
    print("a quantidade de "+ str(amount[i]) + " " + product[i] + "ao preço de "+ str(price[i]) + " cada, vai custar " + str(total_price) + " reais")
    i = i +1
    

