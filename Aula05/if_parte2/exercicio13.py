# Exercicio 13
# 
# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.
# 
# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.
# 
# Se o usuário selecionar "Dados" deve aparecer o nome do cliente e a idade
# 
# Se o usuário selecionar "Endereço" deve aparecer o nome do cliente e o endereço
# 
# Se o usuário selecionar "Contato" deve aparecer o nome do cliente, email e o telefone

name = input("Informe seu nome: ")
age = int(input("Informe sua idade: "))
address = input("Informe seu endereço: ")
email =input("Informe seu email: ")
phone = input("Informe seu numero de telefone: ")

print("""

O que deseja acessar?

(1)Dados: Nome e idade    
(2)Endereço: Nome e endereço
(3)Contato: Nome, email e telefone

""")
chosen = int(input())

if (chosen == 1):
    print("Nome: "+name)
    print("Idade: "+age)
elif(chosen == 2):
    print("Nome: "+name)
    print("Endereço: "+address)
elif(chosen == 3):
    print("Nome: "+name)
    print("email: "+email)
    print("Endereço: "+address)
else:
    print("Escolha uma opção valida")
