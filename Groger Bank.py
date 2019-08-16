nome = input('Seu nome completo: ')
idade = int(input('Sua idade: '))
saldo = float(input('Seu Saldo: '))

print('Digite (1) para saque')
print('Digite (2) para depósito')
print('Digite (3) para empréstimo')
print('Digite (4) para visualizar informações')
print('Digite (Qualquer outro texto ou número) para sair')

menu = input('Digite aqui: ')

if menu == '1':
    print('SAQUE')
    valor_saque = float(input('Digite o valor o valor desejado para saque:'))
    if (valor_saque > 1000) or (valor_saque >= float(saldo)):
        print('Saque indiponível, valor indisponível ou acima de R$1000,00')
    else:
        saldo_atual = saldo - valor_saque
        print('SAQUE REALIZADO')
        print(f'SALDO ATUAL É DE {saldo_atual}')

# elif menu == 2:
#
#
# elif menu == 3:
#
#
# elif menu == 4:
#
#
# else:
#
