palavras = []
contr = []
palavra = ""
for i in range (1,6):
    palavras.append(input(f"Insira a {i}° palavra: "))
for i in range (0,5):
    palavra = palavras[i][::-1]
    contr.append(palavra)
print ("\nPolíndromos:")
for i in range (0,5):
    if contr[i] == palavras[i]:
        print (contr[i])