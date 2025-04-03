anoatual = 2025
nasc = int(input("Insira seu ano de nascimento: "))
idade = anoatual - nasc
if idade >= 18:
    vip = input("Você é membro? 1 - SIM/ 2 - NÃO: \n").lower()
    if vip == "1" or vip == "sim":
        print("Seja bem-vindo")
    else:
        vip2 = input("Você está acompanhado por algum membro? 1 - SIM/ 2 - NÃO: \n")
        if vip2 == "1" or vip2 == "sim":
            print("Pague meia entrada")
        else:
            print("Pague uma inteira.")
else:
    print("Menor de idade. Não pode entrar")