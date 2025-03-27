print ("Olá, seja-bem vindo à seção de cadastro")
senha = input("Insira sua senha: ")
conf = len(senha)
if conf >= 8:
    email = input("Insira seu email: ").lower()
    print("cadastro realizado com sucesso")
    print ("Bem-vindo novamente, faça seu cadastro")
    senha2 = input("Insira sua senha: ")
    email2 = input("Insira seu email: ").lower()
    if email2 == email and senha2 == senha:
        print("Login realizado com sucesso")
    else:
        print("Login ou senha incorretos.")
else:
    print ("Senha menor que 8 caracteres. Comece de novo")