# 3) Estas 3 listas:

# Estas listas são referente as vendas dos vendedores Armando, Paulo e Eduardo.

# 3.1) Com base nelas e usando funções da lista mostradas em aula, mostre:
# A média de vendas de cada um;
# A venda total de cada vendedor;
# A quantidade de vendas de cada vendedor.

# 3.2) Calcule o valor de comissão que o dono da loja deve pagar para seus funcionários seguindo a regra:

# Para total de vendas de 0.00 a 1000.00 Reais - 1%
# Para total de vendas de 1000.01 a 2500.00 Reais - 1.5%
# Para total de vendas de 2500.01 a 5000.00 Reais - 2%
# Para total de vendas a cima de 5000.01 Reais - 3%

vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
vendas_paulo = [950.00, 89.90, 2500.00, 1750.00,500.00]

mediaA = sum(vendas_armando) / len(vendas_armando)
mediaE = sum(vendas_eduardo) / len(vendas_eduardo)
mediaP = sum(vendas_paulo)  / len(vendas_paulo)

print(" ")
print("A media de venda de armando, paulo e eduardo são, respectivamente: \n"+ str(mediaA) + ";  \n" + str(mediaE)+ ";  \n" +str(mediaP))
print(" ")
print("A venda total de armando, paulo e eduardo são, respectivamente: \n"+ str(sum(vendas_armando)) + ";  \n" + str(sum(vendas_eduardo))+ ";  \n" +str(sum(vendas_paulo)))
print(" ")
print("A quantidade de vendas de armando, paulo e eduardo são, respectivamente: \n"+ str(len(vendas_armando)) + ";  \n" + str(len(vendas_eduardo))+ ";  \n" +str(len(vendas_paulo)))
print(" ")
print("3.2")


vendedores = [vendas_armando, vendas_eduardo, vendas_paulo]

for i in vendedores:
    if(sum(i) < 1000):
        taxa = 1
    elif(sum(i) < 2500):
        taxa = 1.5
    elif(sum(i) < 5000):
        taxa = 2
    else:
        taxa = 3
    print("Para " + str(i) + " a taxa sera de " + str(sum(i)*taxa/100) + "com "+ str(taxa) +" % de comissão")
