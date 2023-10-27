produtos = []
print('CADASTRO DOS PRODUTOS')
print()
print('Digite pare no campo de nome para parar.')
while True:
    aux = input('Nome do Produto: ')
    if aux == 'Pare':
        break
    produtos.append(aux)
    aux2 = input('Valor (R$) do produto: ')
    produtos.append(aux2)
print('PRODUTOS CADASTRADOS')

