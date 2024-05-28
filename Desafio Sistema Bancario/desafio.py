menu = """

[d] Depositar
[s] Sacar
[e] Extrato 
[q] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n" 
        else:
            print("O valor informado não é válido.")
    
    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")
        elif excedeu_limite:
            print("O valor do saque excede o limite")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}"
            numero_saques += 1
        else:
            print("O valor informado não é válido.")

        
    elif opcao == "e":
        print("################ Extrato ################")
        if not extrato:
            print(f"\nSem movimentações na sua conta.")
            print(f"\nSaldo: R$ {saldo:.2f}")
        else:
            print(f"\n{extrato}")
            print(f"\nSaldo: R$ {saldo:.2f}")
        print("#########################################")
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
     