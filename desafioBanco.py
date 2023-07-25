menu = '''

[1] DEPOSITO
[2] SAQUE
[3] EXTRATO
[4] SAIR

'''
saldo = 0
limite = 500
extrato = ""
credito_extra = 0
numero_saques = 0
LIMITE_SAQUES = 3
ESPECIAL = 500

while True:

    opcao = input(menu)

    if opcao == '1':
        valor = float(input('Informe o valor a ser depositado: '))
        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R${valor:.2f}\n'
        else:
            print('Operação irregular')    

    elif opcao == '2':
        valor = float(input('Digite o valor do saque: '))
        
        excede_saldo = valor > saldo
        excede_limite = valor > limite
        excede_saque = numero_saques >= LIMITE_SAQUES
        
        if excede_saldo:
            opcao_credito = int(input('''Saldo insuficiente, digite 1 para realizar um emprestimo, ou 2 para sair: '''))
            if opcao_credito == 1 :
                    credito_extra = float(input(f'Digite valor do emprestimo, limite de R${limite:.2f} :  '))
                    saldo += credito_extra
                    if credito_extra >= ESPECIAL:
                        print('Não e possivel realizar o emprestimo!')
   
            else:
                 print('Voltando ao Menu!')
        elif excede_limite:
            print('limite do dia alcançado!')

        elif excede_saque:
             print('Pois e, não pode mais sacar!')
        
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$: {valor:.2f}\n'
            numero_saques += 1
        
        else:
            print('Não deu certo, valor invalido!')

    elif opcao == '3':
        print('\n*******************Extrato*********************')

        print('Não foram realizadas operaçoes de deposito/saque.' if not extrato else extrato)

        print(f'\nSaldo no credito especial: R$ {credito_extra:.2f}')

        print(f'\nSaldo total: R$ {saldo:.2f}')

        print('***********************************************')


    elif opcao == '4':
        break
    else:
        print('Opção Invalida')            


