print('~' * 21)
print('  GERADOR DE MOEDAS')
print('~' * 21)

while True: 
    valor = float(input('Digite o valor que deseja converter: R$ '))
    opc = input('Eis as opções de conversão: \n[DO] para converter real em dólar\n[EU] para converter real para euro.\nQual a sua escolha? Qual a sua escolha? ').upper()
    while opc not in 'DOEU':
        print('ERRO! Digite apenas DO ou EU.')
        opc = input('Eis as opções de conversão: \n[DO] para converter real em dólar\n[EU] para converter real para euro.\nQual a sua escolha? Qual a sua escolha? ').upper()
    if opc == 'DO':
        dolar = valor / 5.71
        print(f'O valor R$ {valor:.2f} convertido em dólar, considerando a cota de 5.71 resultou em US$ {dolar:.2f}.')
    if opc == 'EU':
        euro = valor / 6.16
        print(f'O valor R$ {valor:.2f} convertido em euro, considerando a cota de 6.16 resultou em € {euro:.2f}.')
    opc2 = input('Gostaria de continuar? (S/N) ').upper()
    while opc2 not in 'SN':
        print('ERRO! Digite apenas S ou N.')
        opc2 = input('Gostaria de continuar? (S/N) ').upper()
    if opc2 == 'N':
        break
print('<< VOLTE SEMPRE! >>')
