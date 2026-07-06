g=input("Digite o gênero (M - masculino / F - Femino) " ).upper()
i=int(input("Digite a idade "))
print(f"sexo {g} idade {i}")
if g == "M" and i >=18:
    print("Candidato apto a se alistar")
else:
    print("não apto")

