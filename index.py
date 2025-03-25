# #Isso é um comentário (seleciona+ctrl+; = transforma em comentário)
# print ("Mensagem")
# idade= 6
# altura= 0.50 #vírgula ñ funciona
# peso= 5.950
# nome= "Francisco"
# print (idade, altura, peso, nome)

# nome = input ("Insira seu nome")
# idade = int(input("Insira sua idade"))
# peso = float(input("Insira seu peso"))
# print(f"{nome} {idade} anos {peso}kg") #f é para formatar

# pedaco_pizza = 5.0
# cliente = "John"
# print (type(pedaco_pizza))
# print (type(cliente))
# #//type= mostra o tipo da variável

# pedaco_pizza = input("Informe quantos pedaoes de pizza comeu")
# print (type(pedaco_pizza))

# a = 4
# A = "Sally"
# print(a)
# print(A)

# fruta1, fruta2, fruta3 = "Laranja", "Banana", "Maça"
# print(fruta1,fruta2,fruta3)

# primeiro_numero=5
# segundo_numero=10
# print(primeiro_numero+segundo_numero)

# nome=input("Qual o vingador mais forte? ")
# print(f"Olá,{nome}!")
# if nome == "hulk":            #//(==)Comparação (=)Atribuição
#     print("Bem-vindo, vingador mais forte")
# else:
#     print("Acesso negado")

# n1= str(input("Insira o 1: "))
# n2= str(input("Insira o 2: "))
# print (n1+n2)

# x = 5
# if x > 2 and x < 10:
#     print("O número está entre 2 e 10.")
# else:
#     print("Não está entre 2 e 10.") 

# x = 5
# if x < 2 or x > 4:
#     print("O número é menor que 2 ou maior que 4.")

# x = 5
# if not x > 10:
#     print("O número não é maior que 10")

x = 5
y = 8
if x > 2 and (y>10 or not x ==5):
    print ("Condição complexa atendida.")
else:
    print("Condição não atendida.")
#   A ordem na qual Python avalia os operadores lógicos é 1.not 2.and 3.or  