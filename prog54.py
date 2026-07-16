def idade_nasc(ano):
	idade = 2026 - ano
    if idade >= 65:
        print("Idoso")
    elif idade >=18 and idade  < 65:
	   print("Maior de idade")
    else:
	   print("Menor de idade")
i=int(input("Digite o ano de nascimento"))
idade_nasc(i)