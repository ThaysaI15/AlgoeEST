numeros = []
for i in range (1, 6):
    num = int(input(f"Insira o {i}° número: "))
    numeros.append(num)
menor = numeros[0]
maior = numeros[0]
for i in range (0, 5):
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]
print (f"Maior = {maior}\nMenor = {menor}")