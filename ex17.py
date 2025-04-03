anoatual = 2025
nasc = int(input("Insira seu ano de nascimento: "))
idade = anoatual - nasc
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")