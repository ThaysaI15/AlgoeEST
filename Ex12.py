print ("Aviso, estamos verificando os saldos da conta. Contas zeradas serão encerradas!")
conta = bool(True)
saldo = float(input("Por favor, insira o saldo da conta: "))
if saldo <= 0:
    conta = False
    print ("Esta conta foi encerrada\nConta inativa")
else:
    print ("Conta permanece ativa")