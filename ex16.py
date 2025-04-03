n1 = float(input("Insira a primaira nota: "))
n2 = float(input("Insira a segunda nota: "))
n3 = float(input("Insira a terceira nota: "))
md = (n1+n2+n3)/3
if md >= 7:
    print ("Aluno aprovado")
else:
    if md < 7 and md >= 5:
        print ("Aluno em recuperação")
    else:
        print("Aluno reprovado")