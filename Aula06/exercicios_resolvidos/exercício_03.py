
print("""

A) soma
B) média
C) divisão
D) Sair

""")
choosen = input("O que deseja fazer? ")

if(choosen == "A" or choosen == "a"):

    n1 = int(input("Diga o primeiro numero: "))
    n2 = int(input("Diga o segundo numero: "))
    print(n1 + n2)

elif(choosen == "B" or choosen == "b"):
    n1 = int(input("Diga o primeiro numero: "))
    n2 = int(input("Diga o segundo numero: "))
    n3 = int(input("Diga o terceiro numero: "))
    n4 = int(input("Diga o quarto numero: "))
    print((n1 + n2 + n3 + n4)/4)
elif(choosen == "C" or choosen == "c"):
    n1 = int(input("Diga o primeiro numero: "))
    n2 = int(input("Diga o segundo numero: "))
    if n2 is 0:
        print("Erro! Não pode dividir por ZERO!")
    else:
        print(n1/n2)    
else:
    print("Muito Obrigado e Volte sempre!")

