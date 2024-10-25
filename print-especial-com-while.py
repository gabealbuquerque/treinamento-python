def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print('-' * tamanho)
    print(f'  {mensagem}')
    print('-' * tamanho)
 

while True:
    mensagem = input('Escreva uma mensagem: ')
    escreva(mensagem)
    opc = input('Gostaria de continuar? [S/N]').upper()
    if opc in 'N':
        break
    if opc not in 'SN':
        print('Erro! Digite apenas S ou N.')
        opc = input('Gostaria de continuar? [S/N]').upper()
print('<< VOLTE SEMPRE! >>')
