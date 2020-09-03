"""Exercício 02

O id de um cliente é um código único (só aquela pessoa tem) composto por números inteiros que inicia do número 1 e vai aumentando de 1 em 1 enquanto for necessário.

Exemplo:
id: 1
Nome: Dudu

id: 2
Nome: Marta

id: 3
Nome: Pedro


ATENÇÃO!!!!
O id é um número atribuido automáticamente! O cliente não escolhe o número. O seu programa deve fazer o cadastro deste id automaticamente.


Com isso, crie um cadastro de clientes que receba o id, nome e idade. Depois mostre os dados dos clientes individualmente.
(cadastre no minimo 4 clientes)
"""
nomes = []
idades = []
identificadores = []

for i in range(4):
    nome = str(input("diga seu nome"))
    idade = str(input("diga sua idade"))

    nomes.append(nome)
    idades.append(idade)
    identificadores.append(i)


for i in range(4):
    print(f'''
    ***********************************
    Relatório de clientes cadastrados 
    ***********************************
    Nome: {nomes[i]}
    Idade: {idades[i]}
    id:  {identificadores[i]}
    ***********************************
    ''')