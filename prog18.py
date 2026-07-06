cargo=input("Digite seu cargo ").upper()
if cargo == "CAIXA":
    s=1500
elif cargo == "VENDEDOR":
    s=2400
elif cargo == "GERENTE":
    s=4000
else:
    s=0
    print("Cargo não existe, digite um cargo válido")
inss= s * 0.12
#irrf
if s > 2000:
    irrf = s * 0.14
else:
    irrf = s * 0.08
#fim do irrf
sf = s - irrf - inss
print(f"Querido seu cargo de {cargo} tem o salário de {s} e os impostos são: ")
print(f"INSS -> {inss}")
print(f"IRRF -> {irrf}")
print(f"Seu salário final é {sf}")

