produtos = []
print('CADASTRO DOS PRODUTOS')
print()
print('Digite pare no campo de nome para parar.')
while True:
    print()
    aux = input('Nome do Produto: ')
    if aux == 'pare':
        break
    produtos.append(aux)
    aux = input('Valor (R$) do produto: ')
    produtos.append(aux)

print()
print('PRODUTOS CADASTRADOS')

for a in range(0,len(produtos),2):
    print()
    print(produtos[a])
    print(f'Valor:R${produtos[a+1]}')