# Exercicio 5
# Faça um programa que peça uma senha ao usuário.
# 
# Se a senha for igual a "Abacaxi" deve aparecer a mensagem "Entrada liberada"
# 
# Caso contrário deve aparecer a mensagem "Senha incorreta"

senha = "Abacaxi"
tentativa = input("diga sua senha: ")

if (tentativa == senha):
    print("Entrada liberada")
else:
    print("Senha incorreta")
