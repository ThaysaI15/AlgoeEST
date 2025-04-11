# 26. Cálculo de Média
# - Crie uma lista chamada notas com as notas de 5 alunos fornecidas pelo usuário.
# - Use um laço for para calcular a média das notas.
# - Exiba a média no final.
media = float(0)
# notas = []
alunos = []
for i in range (0,5):
    alunos.append (input("Insira o nome do aluno(a): "))
    nota = float(input(f"Insira a nota do(a) aluno(a) {alunos[i]}: "))
    # notas.append (nota)
    media = media+nota
media = media/5
print (f"A média de notas foi: {media}")