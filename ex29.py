# 29. Multiplicação de Elementos da Lista
# - Crie uma lista chamada valores com 4 números inteiros fornecidos pelo usuário.
# - Peça ao usuário um número adicional e multiplique cada elemento da lista pelo número fornecido, usando um laço for.
# - Exiba os novos valores da lista.
valores = []
for i in range (1,5):
    valor = int(input(f"Insira o {i} número: "))
    valores.append(valor)
num = int(input("Insira o valor a multiplicar: "))
for i in range(0,4):
    valores[i] = valores[i]*num
    print (valores[i])