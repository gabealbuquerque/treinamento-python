def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print('-' * tamanho)
    print(f'  {mensagem}')
    print('-' * tamanho)

mensagem = input('Escreva uma mensagem: ')
escreva(mensagem)
