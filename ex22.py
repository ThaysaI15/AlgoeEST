palavras = []
for i in range(0,6):
    palavra = input("Insira a palavra: ")
    palavras.append (palavra)
total = 0
for i in range(0,6):
    if (len(palavras[i])) == 5:
        total = total+1
print (f"A quantidade de palavras com 5 caracteres é igual a {total}")