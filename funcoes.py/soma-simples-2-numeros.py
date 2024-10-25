def soma(a, b):
    soma = a + b
    print(f'A soma do valor {a} + {b} = {soma}')

while True:
    a = int(input('Digite o primeiro valor a ser somado: '))
    b = int(input('Digite o segundo valor a ser somado: '))
    soma(a, b)
    opc = input('Quer continuar? [S/N]' ).upper()
    if opc not in 'SN':
        print('ERRO! Digite apenas S ou N.')
        opc = input('Quer continuar? [S/N] ').upper()
    if opc in 'N':
        break
print('<< VOLTE SEMPRE! >>')
