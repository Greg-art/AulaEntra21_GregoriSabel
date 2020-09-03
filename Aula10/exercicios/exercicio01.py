'''
Exercício 01

Crie um programa que cadastre 5 clientes. 

Cada cliente possui: Nome, sexo, Telefone
(Guarde estes dados em listas separadas).

Depois mostre os dados cadastrados no seguinte formato:

***********************************
Relatório de clientes cadastrados 
***********************************
Nome: 
Sexo:
Telefone:
***********************************
'''

nomes = []
sexos = []
telefones = []

for i in range(5):
    nome = str(input("diga seu nome"))
    sexo = str(input("diga seu sexo"))
    telefone = str(input("diga seu telefone"))
    
    nomes.append(nome)
    sexos.append(sexo)
    telefones.append(telefone)

for i in range(5):
    print(f'''
    ***********************************
    Relatório de clientes cadastrados 
    ***********************************
    Nome: {nomes[i]}
    Sexo: {sexos[i]}
    Telefone:  {telefones[i]}
    ***********************************
    ''')