# Exercicio 16
# 
# Crie um programa para uma promoção de um posto de combustivel.
# 
# O programa deve pedir ao usuário quantos litros ele quer abastecer e qual combustivel: álcool, diessel ou gasolina
# 
# A promoção é a seguinte:
#  - Para gasolina: Até 20 litros 0% de desconto e acima de 20 litros 10% de desconto
#  - Para diessel: Até 10 litro 1.5% de desconto e acima de 10 litros 5% de desconto
#  - para álcool: Até 10 litros 5% de desconto e acima de 10 litros 10% de desconto.
#  
# Mostre o combustivel que ele selecionou, o total abastecido e a porcentagem de desconto a ser aplicada.
# 
# Não precisa calcular o valor do combustivel!
# 
print("""

escolha o tipo de combustivel:
(1)gasolina  -  (2)diesel  -  (3)álcool

""")

chosen = int(input())

print("""

quantos litros gostaria?

""")

amount = int(input())

if chosen is 1: 
    combus = "gasolina"
    off = 10 if (amount > 20) else 0
elif chosen is 2:
    combus = "diesel"
    off = 5 if (amount > 10) else 1.5
else:
    combus = "álcool"
    off = 10 if (amount > 10) else 5

print("Você comprara "+ str(amount) + " litros de "+combus+" e ganhará "+str(off)+"% de desconto")