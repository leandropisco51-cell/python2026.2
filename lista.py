nomes = ["joão","Ana","Bruno"] #array, matriz ou vetor
print(f"Listagem de nomes {nomes}")
nomes.append("Carlos")
print(f"Listagem de nomes ATUALIZADA {nomes}")
n=input("Digite um nome a ser excluido => ")
nomes.remove(n)
print(f"Listagem de nomes ATUALIZADA Excluisão {nomes}")
nomes.sort()
print(f"Listagem de nomes ORDENADA {nomes}")
l = len(nomes)
print(f"A lista em {l} itens")


