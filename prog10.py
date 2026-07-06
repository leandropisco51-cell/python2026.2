nome=input("Digite um nome ")
n1=float(input("Digite a primeira nota "))
n2=float(input("Digite a segunda nota "))
n3=float(input("Digite a terceira nota "))
n4=float(input("Digite a quarta nota "))
m = (n1+n2+n3+n4)/4
print(f"{nome} sua média é {m}")
if m >= 6:
    print("Aprovado")
else:
    print("Recuperação")
