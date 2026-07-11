carros={}
for i in range(2):
    carro=input("Digite o carro ")
    marca=input("Digite o marca ")
    valor=float(input("Digite o valor "))
    carros[carro] = {
        "marca": marca,
        "valor": valor
    }   
print(f"Lista de carros {carros}")
