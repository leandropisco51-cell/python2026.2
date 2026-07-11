nome="" 
while nome != "SAIR":
    nome=input("Digite um nome ").upper()
    if nome=="SAIR":
        break
    print(f"olá {nome} tudo bem? ")
