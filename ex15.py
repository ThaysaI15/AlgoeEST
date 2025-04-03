print ("Seja bem-vindo ao mercado")
nome = input("Insira o nome do produto: \n")
qnt = int(input("Insira a quantidade do produto: \n"))
valor = float(input("Insira o valor do produto(unidade): \n"))
total = qnt*valor
if total > 100:
    total = total - total * 0.05
    print (f"Valor total: R$ {total}")
else:
    print (f"Valor total: R$ {total}")