anoa = int(input("Digite o ano de nascimento "))
idade = 2026 - anoa
if idade >= 65:
    print(f"sua é idade é {idade} Maior de idade")
elif idade >= 18:
    print(f"sua é idade é {idade}  Idoso")
else:
    print(f"sua é idade é {idade} Menor de idade")
