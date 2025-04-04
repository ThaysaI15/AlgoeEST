idade = int(input("\nInsira sua idade: "))
if idade < 15:
    print ("\nArtigos infantis\n")
else:
    gen = input("\nQual seu gênero?\n 1 - FEMININO // 2 - MASCULINO: ")
    if gen == "2":
        atleta = input("\nÉ atleta?\n 1 - SIM // 2 - NÃO: ")
    if gen == "1" and idade <= 21:
        print("\nMaquiagem e moda\n")
    if gen == "2" and atleta == "1" and idade <= 32:
        print("\nArtigos esportivos\n")
    if gen == "2" and atleta == "2" and idade <= 21:
        print("\nVideogames\n")
    if gen == "2" and atleta == "2" and idade > 21 and idade <= 32:
        print("\nLivros, jardinagem e eletrodomésticos\n")
    if gen == "1" and idade > 21 and idade <= 35:
        print("\nArtigos esportivos e itens de casa\n")
        