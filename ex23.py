num = int(input("Insira um número inteiro: "))
tabuada = []
for i in range (1,11):
    tabuada.append(num*i)
    print (f"{num} x {i} = {num*i}")
