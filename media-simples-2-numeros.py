def media(a, b):
    media = (a + b) / 2
    print(f'A media de {a} + {b} / 2 = {media}')

while True:
    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))
    media(a, b)
    opc = input('Quer continuar? [S/N] ').upper()
    if opc not in 'SN':
        print('ERRO! Digite apenas S ou N.')
        opc = input('Quer continuar? [S/N] ').upper()
    if opc in 'N':
        break
print('<< VOLTE SEMPRE! >>')
