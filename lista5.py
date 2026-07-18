mercado=[]
item=""
while item != "sair":
    item=input("Digite um item ").lower()
    if item == "sair":
        break
    if item in mercado:
        print("item já cadastrado")
    else:
        mercado.append(item)
        for i in mercado:
            print(i)