"""Exercício 4

(use o conhecimento que foi passado no curso)

Crie um programa com um menu interativo:

-----
Cadastro de pessoas v1.0

A) Cadastrar Pessoa
B) Ver todos os nomes cadastrados:
C) Ver cadastro pelo nome:
D) Apagar um cadastro pelo nome:
S) Sair

-----


Para A: Cadastre os dados do cliente (Nome, idade, sexo, telefone
Para B: Mostre todos os nomes dos clientes (só os nomes)
Para C: Digite o nome do cliente e mostre todos os dados dele.
Para D: Digite o nome do cliente e o apague do cadastro
Para S: Mostre uma mensagem de despedida e termine o programa
Para qualquer outro valor: Mostre "Opção invalida"
"""

import time 

nomes     = []
idades    = []
sexos     = []
telefones = []
i = " "
while (i != "s" and i != "s" ):
    time.sleep(1)
    print('''
    -----
    Cadastro de pessoas v1.0

    A) Cadastrar Pessoa
    B) Ver todos os nomes cadastrados:
    C) Ver cadastro pelo nome:
    D) Apagar um cadastro pelo nome:
    S) Sair

    -----

    ''')
    i = input("O que deseja fazer: ")

    if (i == "a" or i == "A"):
        nomes.append(input("Diga seu nome: "))
        idades.append(input("Diga sua idade: "))
        sexos.append(input("Diga seu sexo: "))
        telefones.append(input("Diga seu telefone: "))

    elif(i == "b" or i == "B"):
        print(nomes)
    elif(i == "c" or i == "C"):
        nome = input("Deseja ver os dados de quem? ")
        posicao = int(nomes.index(nome))
        print("nome: "+ nomes[posicao])
        print("idade: "+ idades[posicao])
        print("sexo: "+ sexos[posicao])
        print("telefone: "+ telefones[posicao])

    elif(i == "d" or i == "D"):
        nome = input("Deseja apagar o cadastro de quem? ")
        posicao = int(nomes.index(nome))
        del(nomes[posicao])
        del(idades[posicao])
        del(sexos[posicao])
        del(telefones[posicao])

    elif(i == "s" or i == "S"):
        print("Até mais e volte sempre! ")
    else:
        print("Opção invalida")