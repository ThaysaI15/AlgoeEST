nome = input("Insira o nome: ")
idade = input(int("Insira a idade: "))
turma = input("Insira a turma: ")
print (f"Aluno cadastrado com sucesso {nome}, {idade} anos. Turma {turma}")
if idade >= 6:
    print("matrícula validada")