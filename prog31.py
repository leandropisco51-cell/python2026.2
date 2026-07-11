for i in range(4):
    print(f"--- Controle de Aluno  ---")
    nome = input("Digite o nome do aluno: ")    
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))  
    media = (nota1 + nota2 + nota3) / 3  
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado" 
    print("--- Resultado ---")
    print(f"Aluno: {nome}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")