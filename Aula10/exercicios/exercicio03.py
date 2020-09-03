"""Exercício 03

3.1) Crie um programa que cadastre o id, nome, sexo e a idade de 5 clientes.

3.2) Depois mostre os dados dos 5 clientes.

3.3) Peça para que o usuário escolha um id de um cliente e mostre as informações deste cliente.

3.4) Crie um filtro que ao digitar um id de um cliente mostre as seguintes informações:
- Para menores de 17 anos: Entrada Proibida
- Para maiores de 17 anos: Entrada Liberada
- Para o sexo Feminino: 50% de desconto
- Para o sexo Masculino: 5% de desconto
"""

nomes = []
sexos = []
idades = []
identificadores = []

for i in range(2):
    nome = str(input("diga seu nome:"))
    sexo = str(input("diga seu sexo (M para mulher e H para homem): "))
    idade = int(input("diga sua idade: "))

    nomes.append(nome)
    sexos.append(sexo)
    idades.append(idade)
    identificadores.append(i)


for i in range(2):
    print(f'''
    ***********************************
    Relatório de clientes cadastrados 
    ***********************************
    Nome: {nomes[i]}
    Sexo: {sexos[i]}
    Idade: {idades[i]}
    id:  {identificadores[i]}
    ***********************************
    ''')


for x in range(10):
    print("escolha um cliente para mais informações")
    i = int(input("escolha pelo id: "))


    print(f'''
        ***********************************
        Relatório de clientes cadastrados 
        ***********************************
        Nome: {nomes[i]}
        Sexo: {sexos[i]}
        Idade: {idades[i]}
        id:  {identificadores[i]}
        ***********************************
        ''')

    if((idades[i]) < 17):
        print("ENTRADA PROIBIDA")
    else:
        print("ENTRADA LIBERADA")

    if((sexos[i]) == "M"):
        print("50% de desconto\n")
    else:
        print("5% de desconto\n")
