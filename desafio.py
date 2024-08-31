saldo = 0
limite = 0  
LIMITE_SAQUE = 3
hitorico_saque = []
hitorico_deposito = []

def depositar(deposito):
    print("_____________________________________________________________")
    global saldo
    if deposito <= 0:
        print("Operação inválida: Depósito não pode ser inferior ou igual a 0")
    else:
        saldo += deposito
        print(f"Deposito de R$ {deposito:.2f} realizado com sucesso!")
        hitorico_deposito.append(deposito)
    print("____________________________________________________________")


def saque_dinheiro(saque):
    print("_________________________________________________________")
    global LIMITE_SAQUE
    global saldo
    global limite
    
    if saque > 500:
        print("Não é possível fazer saque superior a R$ 500,00!")
    elif saque > saldo:
        print("Não é possível sacar dinheiro por falta de saldo!")
    elif limite >= LIMITE_SAQUE:
        print(f"Limite de {LIMITE_SAQUE} saques diários atingido!")
    else:
        saldo -= saque
        limite += 1
        print(f"Saque de R$ {saque} realizado com sucesso!")
        hitorico_saque.append(saque)
    print("___________________________________________________________")


def extrato():
    print("____________________________")
    global saldo
    print("Extrato Geral:")
    print("Deposito:")
    for deposito in hitorico_deposito:
        print(f"R$ {deposito:.2f}")
    print("\n")
    print("Saques:")
    for saque in hitorico_saque:
        print(f"R$ {saque:.2f}")    
    print("\n")
    print(f"Saldo Atual: {saldo:.2f} ")
    print("____________________________")




while True:
    print(""" 
|    [1] Depositar |
|    [2] Sacar     |
|    [3] Extrato   |
|    [4] Sair      |
####################      
""")
    opcao = int(input("Digite uma opção:"))
    print("\n")

    if opcao == 1:
        deposito = float(input("Digite o valor do depósito: "))
        depositar(deposito)

    elif opcao == 2:
        saque = float(input("Digite o valor do saque: "))
        saque_dinheiro(saque)
        
    elif opcao == 3:
        extrato()

    elif opcao == 4:
        print("Programa Finalizado!")
        break

    else:
        print("Opção inválida! Tente novamente.")
