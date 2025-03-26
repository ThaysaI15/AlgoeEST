print ("Caro cliente, seja bem-vindo à seção de descontos do mercado! Aqui você pode garantir descontos imperdíveis de acordo com o valor da sua compra:\nAcima de R$100,00 = 5% \nAcima de R$250,00 = 10% \nAcima de R$500,00 = 25%")
preco = float(input("Insira o valor total da compra: "))
if preco >= 100 and preco < 250:
    print("Parabéns, você adquiriu um desconto de 5% na sua compra!\nValor do desconto: R$", preco*0.05)
    desc = print("Valor total com o desconto: R$", preco-preco*0.05)
if preco >= 250 and preco < 500:
    print("Parabéns, você adquiriu um desconto de 10% na sua compra!\nValor do desconto: R$", preco*0.1)
    desc = print("Valor total com o desconto: R$", preco-preco*0.1)
if preco >= 500:
    print("Parabéns, você adquiriu um desconto de 25% na sua compra!\nValor do desconto: R$", preco*0.25)
    desc = print("Valor total com o desconto: R$", preco-preco*0.25)
if preco < 100:
    print ("Sua compra não atingiu o valor mínimo para receber os descontos, portanto o valor total de sua compra ficou em: R$",preco)