# 28. Filtrando Números Pares e Ímpares
# - Crie uma lista chamada numeros com 8 números inteiros escolhidos pelo usuário.
# - Use um laço for para dividir os números em duas listas: pares e impares.
numeros = []
par, impar = [],[]
for i in range(1,9):
    numero = int(input(f"Insira o {i}° número: "))
    numeros.append(numero)
    rest = numero%2
    if rest == 0:
        par.append(numero)
    else:
        impar.append(numero)
print (f"Números Pares:\n{par}")
print (f"\nNúmeros ímpares\n{impar}")