# Tabela de Produtos para referência:
# 001 -> Arroz   (R$ 4.00)
# 002 -> Feijão  (R$ 7.00)
# 003 -> Macarrão (R$ 5.00)

total_compra = 0
codigo = "1"  # Começa com "1" apenas para o while aceitar entrar no laço

print("--- CAIXA DE SUPERMERCADO SIMPLES ---")
print("Produtos: 001 (Arroz: R$4) | 002 (Feijão: R$7) | 003 (Macarrão: R$5)")
print("Digite 0 para encerrar a compra.\n")

# O laço continua rodando enquanto o código digitado não for "0"
while codigo != "0":
    codigo = input("Digite o código do produto (ou 0 para parar): ")
    
    # Verificação de cada produto usando IF
    if codigo == "001":
        print("-> Adicionado: Arroz (R$ 4.00)")
        total_compra = total_compra + 4.00
        
    if codigo == "002":
        print("-> Adicionado: Feijão (R$ 7.00)")
        total_compra = total_compra + 7.00
        
    if codigo == "003":
        print("-> Adicionado: Macarrão (R$ 5.00)")
        total_compra = total_compra + 5.00
        
    # Mensagem extra caso o aluno digite um código errado (opcional, mas bom para aprender)
    if codigo != "001" and codigo != "002" and codigo != "003" and codigo != "0":
        print("⚠️ Código inválido! Tente novamente.")

print("--- COMPRA FINALIZADA ---")
print(f"Total a pagar: R$ {total_compra:.2f}")