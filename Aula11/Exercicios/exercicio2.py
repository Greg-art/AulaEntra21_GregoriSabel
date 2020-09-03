"""Exercício 2

(não usar o continue ou o break)

Crie um menu interativo com as seguintes opções:

A) soma
B) Média
C) Taboada
S) Sair


Para A: Peça 2 números, some e mostr o resultado
Para B: Peça 4 números, faça a média e mostre o resultado
Para C: Peça um número e mostre a taboada dele
Para S: Mostre uma mensagem de despidida e encerre o programa.
Para qualquer outro valor: Mostre a mensagem "opção inválida"
"""

i = 0
while ((i != "S") and (i != "s")):
    print('''

        A) soma
        B) Média
        C) Taboada
        S) Sair

    ''')
    i = input("O que deseja fazer?")
    if (i == "a" or i == "A"):
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite outro numero: "))
        result = n1 + n2
        print(result)
    elif(i == "b" or i == "B"):
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite outro numero: "))
        n3 = int(input("Digite outro numero: "))
        n4 = int(input("Digite outro numero: "))    
        result = (n1 + n2 + n3 + n4)/4
        print(result)
    elif(i == "c" or i == "C"):
        n1 = int(input("Digite um numero: "))     

        for x in range(11):
            print(str(n1*x))

    elif(i == "s" or i == "S"):
        print("Até mais e volte sempre! ")