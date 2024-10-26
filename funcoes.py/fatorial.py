def fatorial(n, show=False):
    """
    Função para calcular o fatorial de um número
    Param n: número a ter o seu fatorial calculado.
    Comando show: mostra o cálculo do fatorial do número.
    Por:
    Gabriel de A. Vasconcelos
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Programa Principal
print(fatorial(5, show = True))
