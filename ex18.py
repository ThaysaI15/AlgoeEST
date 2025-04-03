sal = float(input("Insira o salário: "))
horas = int(input("Insira as horas extras trabalhadas: "))
val = float(input("Insira o valor da hora extra: "))
total = sal + horas * val
print (f"Valor total do salário R${total}")