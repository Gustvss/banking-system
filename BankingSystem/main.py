saldo = 500
limite = 500
Extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    menu = '''
    *************** MENU ***************
    [1] SAQUE
    [2] DEPOSITO
    [3] EXTRATO
    [0] SAIR
    Escolha uma das opções digitando o número desejado:'''
    opcao = int(input(menu))

    if opcao == 1:
        valor_saque = (int(input('    Digite o valor que deseja sacar:')))

        if valor_saque <= limite and saldo and numero_saques < LIMITE_SAQUES:
            print('Saque realizado com sucesso, retire o dinheiro na boca do caixa!')
            numero_saques += 1
            extrato = f"""
            ********* SAQUE BANCO 24HS *********
            Saldo: R${saldo:.2f}
            
            Valor do Saque: -R${valor_saque:.2f}
            """
            Extrato.append(extrato)
            saldo -= valor_saque

        elif valor_saque > saldo:
            print('    Saldo insulficiente!')

        elif valor_saque > limite:
            print(f'    O valor permitido por operação é de R${limite}, tente novamente!')

        else:
            print('    Limite diário de saques atingido, espere até o proximo dia util para realizar um novo saque!')


    elif opcao == 2:
        valor_deposito = (int(input('    Digite o valor que deseja depositar:')))
        print(f'    Deposito no valor de R${valor_deposito} realizado com sucesso!')
        extrato = f"""
            ********* DEPOSITO BANCO 24HS *********
            Saldo: R${saldo:.2f}

            Valor do deposito: +R${valor_deposito:.2f}
            """
        Extrato.append(extrato)
        saldo += valor_deposito


    elif opcao == 3:
        for idx, extrato in enumerate(Extrato, start=1):
            print(f"Extrato {idx}:")
            print(extrato)
            print('-' * 40)

    elif opcao == 0:
        print('    Obrigado por ser nosso cliente, até logo!')
        break

    else:
        print('    Opção inválida, tente novamente!')