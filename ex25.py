import random
palpites = []
random = random.randint(1, 21)
num = 0
while num != random:
    num = int(input("Adivinhe o número! (De 1 até 20): "))
    if num != random:
        print ("Número incorreto")
        palpites.append(num)
print (f"Você acertou!! O número era {random}")
print ("Seus palpites foram = ", palpites)
