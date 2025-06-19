def main():
    print("=" * 25 + " SISTEMA BANCÁRIO " + "=" * 25)
    print("""
[1] - DEPOSITAR
[2] - SACAR 
[3] - EXTRATO
[4] - SAIR
""")


saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
limite = 500

while True:
    main()
    try:
        op = int(input("Bem-vindo! Qual operação deseja realizar? "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue

    if op == 1:
        deposito = float(input("Informe o valor que você deseja depositar: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
        else:
            print("Não é possível depositar valores negativos.")

    elif op == 2:
        saque = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite de R$500.00.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")
        else:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques += 1

    elif op == 3:
        print("\n--- EXTRATO ---")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"Saldo atual: R${saldo:.2f}")

    elif op == 4:
        print("Saindo... Até logo!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")