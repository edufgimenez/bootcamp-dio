

def menu():

    menu = """

    [nc] Nova conta
    [nu] Novo usuário
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [l] Listar contas 
    [q] Sair

    => """

    return input(menu)


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("\nFalha na execução. Saldo insuficiente.")
            
        elif excedeu_limite:
            print("\nFalha na execução. O valor do saque excede o limite")

        elif excedeu_saques:
            print("\nFalha na execução. Número de saques diários excedeu o limite.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"\n\tSaque: R$ {valor:.2f}"
            numero_saques += 1
            print("\nSaque realizado com sucesso!")
        
        else:
            print("\nFalha na execução. O valor informado não é válido.")
        
        return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito: R$ {valor:.2f}"
            print("\n\tDepósito realizado com sucesso!") 
        else:
            print("\n\tFalha na execução. O valor informado não é válido.")
        
        return saldo, extrato
        

def visualizar_extrato(saldo, /, *, extrato):

        print("\n################ Extrato ################")
        
        if not extrato:
            print(f"\nSem movimentações na sua conta.")
            print(f"\n\tSaldo: R$ {saldo:.2f}")
        
        else:
            print(f"\n{extrato}")
            print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n#########################################")


def verifica_se_usuario_existe(cpf, usuarios):
     for usuario in usuarios:
          if usuario['cpf'] == cpf:
               return usuario
     return None

def criar_usuario(usuarios):
     cpf = input("\nInforme o seu CPF sem traços e pontos, utilize apenas números: ")
     usuario = verifica_se_usuario_existe(cpf, usuarios)

     if usuario:
          print("\nFalha na execução. Já existe um usuário cadastrado nesse CPF")
          return
     
     nome = input("\nInforme o seu nome completo: ")
     data_nascimento = input("\nInforme sua data de nascimento (dd/mm/aaaa): ")
     endereco = input("\nInforme seu endereço (logradouro, nro - bairro - cidade/estado): ")

     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

     print("\nUsuario cadastrado com sucesso!")          

def criar_cc(agencia, numero_conta, usuarios):
     cpf = input("\nInforme o seu CPF sem traços e pontos, utilize apenas números: ")
     usuario = verifica_se_usuario_existe(cpf, usuarios)

     if usuario:
          print("\nConta criada com sucesso!")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     
     print("\nFalha na execução. O usuário informado não foi encontrado.")


def listar_contas(contas):
     for conta in contas:
          print(               
               f"""
               Agência: {conta['agencia']}
               C/C: {conta['numero_conta']}
               Titular: {conta['usuario']['nome']}
               """
          )

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("\nInforme o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
    
        elif opcao == "s":
            valor = float(input("\nInforme o valor do saque: "))

            saldo, extrato, numero_saques = sacar (
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
                )
        
        elif opcao == "e":
             visualizar_extrato(saldo, extrato = extrato)

        elif opcao == "nc":
             numero_conta = len(contas) + 1
             conta = criar_cc(AGENCIA, numero_conta, usuarios)

             if conta:
                  contas.append(conta)

        elif opcao == "nu":
             criar_usuario(usuarios)

        elif opcao == "l":
             listar_contas(contas)

        elif opcao == "q":
            break
        
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")
     

if __name__ == "__main__":
     main()
