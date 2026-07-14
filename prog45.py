# Inicializamos a soma zerada
total_soma = 0
numero = 1  # Começamos com 1 apenas para o 'while' aceitar entrar no laço

print("--- SOMADOR DE NÚMEROS ---")
print("Digite os números que quer somar. Digite 0 para ver o resultado.")

# O laço roda enquanto o número digitado for diferente de zero
while numero != 0:
    numero = int(input("Digite um número: "))
    
    # O 'if' garante que só vamos somar se o número não for o zero de saída
    if numero != 0:
        total_soma = total_soma + numero

print("\n--- RESULTADO ---")
print(f"A soma de todos os números digitados é: {total_soma}")