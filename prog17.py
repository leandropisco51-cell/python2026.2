i=int(input("Digite a idade "))
t=input("Já possui o ingresso ? (S-Sim / N-Não)").upper()
if i >=12 and t=="S":
    print("Acesso liberado! Divirta-se no brinquedo.")
elif t=="S" and i<12:
    print("Você tem o ingresso, mas não tem a idade mínima de 12 anos.")
else:
    print("Acesso negado. Você precisa de um ingresso.")
