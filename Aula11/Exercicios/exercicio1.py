"""Exercício 1

(não usar o continue ou o break)

Crie um programa que mostre um memu com as seguites opções:

1) Soma
2) Subtração
3) Multiplicação
S) Para sair!

Para número 1: Peça 2 números e mostre a soma deles
Para número 2: Peça 2 númeors e mostre a subtração deles
Para númeor 3: Peça 2 números e mostre a multiplicação deles
Para S: Mostre uma mensagem de despedida e termine o programa.

Para qualquer outra opção deve aparecer a mensagem "Opção Inválida"
"""
i = 0
while ((i != "S") and (i != "s")):
    print('''

        1) Soma
        2) Subtração
        3) Multiplicação
        S) Para sair!

    ''')
    i = input("O que deseja fazer?")
    if (i == "1"):
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite outro numero: "))
        result = n1 + n2
        print(result)
    elif(i == "2"):
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite outro numero: "))    
        result = n1 - n2
        print(result)
    elif(i == "3"):
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite outro numero: "))
        result = n1 * n2
        print(result)
    elif(i == "s" or i == "S"):
        print("Até mais e volte sempre! ")
        