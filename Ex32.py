def tabuada_personalizada(base, inicio, fim):
    print(f"Tabuada do {base} de {inicio} ao {fim}:")
    for j in range(inicio, fim + 1):
        print(f"{base} x {j} = {base * j}")

# Uso   
base = int(input("Insira o valor para fazer a tabuada: "))  
inicio = int(input("Insira o valor de inicio: ")) 
fim = int(input("Insira o valor de fim: "))        
tabuada_personalizada(base, inicio, fim)