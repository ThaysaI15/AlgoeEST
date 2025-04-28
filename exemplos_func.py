# # tabuada do 7
# print ("Tabuada do 7:")
# for i in range (1,11):
#     print ("7 x", i, "=", 7 * i)

# # tabuada do 8
# print ("Tabuada do 8:")
# for i in range (1,11):
#     print ("8 x", i, "=", 8 * i)

# # tabuada do 9
# print ("Tabuada do 9:")
# for i in range (1,11):
#     print ("9 x", i, "=", 9 * i)

# código em Python para exibir as tabuadas de 7, 8 e 9
def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1,11):
        print (f"{numero} x {i} = {numero * i}")
    
# exibindo as tabuadas
tabuada(7)
tabuada(8)
tabuada(9)

# tabuada escalável em Python
# def tabuada(base):
#     print(f"Tabuada do {base}:")
#     for j in range(1,11):
#         print (f"{base} x {j} = {base * j}")

# # Gerar tabuadas do 1 ao 100
# for i in range(1,101):
#     tabuada(i)

# tabuada personalizada em Python
def tabuada_personalizada(base, inicio, fim):
    print(f"Tabuada do {base} de {inicio} ao {fim}:")
    for j in range(inicio, fim + 1):
        print(f"{base} x {j} = {base * j}")

# Uso              
tabuada_personalizada(7, 1, 10)
tabuada_personalizada(5, 5, 15)