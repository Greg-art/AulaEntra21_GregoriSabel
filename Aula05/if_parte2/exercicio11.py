
# Exercicio 11
# Faça um programa que peça o sexo do cliente. 
# 
# Se o cliente digitar 'F' deve aparecer a mensagem "Como você está bonita hoje!"
# 
# Se o cliente digitar 'M' deve aparecer a mensagem "Como você está forte? andou malhando?"
# 
# Se o cliente digitar qualquer outra coisa, deve aparecer a mensagem: "opção invalida!"
# 

sexo = input("seu sexo (F ou M): ")

if (sexo == "F"):
    print("Como você está bonita hoje!")
elif (sexo == "M"):
    print("Como você está forte? andou malhando?")
else: 
    print("Gostei, diferenciado :)")