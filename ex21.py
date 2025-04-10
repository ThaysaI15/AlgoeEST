numeros = []
for i in range (1,11):
    numero = int(input(f"Insira o {i} número: "))
    numeros.append(numero)
for i in numeros:
    print (numeros[i])
soma = 0 
for i in numeros:
    soma = soma + numeros[i]
print(f"A soma de todos os números é igual a {soma}")