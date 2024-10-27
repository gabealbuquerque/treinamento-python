def notas(*n, sit=False):
    """
    Função para analisar notas e situações de diversos alunos.
    Par n: uma ou mais notas dos alunos(aceita diversas)
    Par sit: valor opcional, indicando se deve ou não adicionar a situação
    Por: Gabriel de A. Vasconcelos
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] > 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
