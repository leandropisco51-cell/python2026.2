n1=int(input("Digite um valor "))
n2=int(input("Digite outro valor"))
print('("1 - Somar")')
print('("2 - Subtrair")')
print('("3 - Multiplicar")')
print('("4 - Dividir")')
e=input("Digite uma das opções acima para operação ")
match e:
    case "1":
        o=n1+n2
    case "2":
        o=n1-n2
    case "3":
        o=n1*n2
    case "4":
        o=n1/n2
    case _:
        o=0
        print("Opção invalida")
print(f"O resultado da operção é {o}")
print("teste de commit")
