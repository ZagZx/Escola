

def q1():
    produtos = {}
    somaq = 0
    soma = 0
    for a in range(0,5):
        print('='*40)
        codigo = int(input('Código do produto: '))
        nome = input('Nome do produto: ')
        qnt = int(input('Quantidade do produto: '))
        preco = float(input('Preço do produto: '))
        produtos[codigo] = [nome,preco,qnt]

    print('========================Relatório=======================')

    
    for a in produtos.keys(): 
        lista = produtos.get(a)
        print(f'Código: {a} | Produto:{lista[0]} | Quantidade:{lista[1]} | Preço: R${lista[2]}')
        aux = produtos[a][1]
        somaq += aux
        soma += aux * produtos[a][2]

    print(f'\nQuantidade total de produtos: {str(somaq)}')
    print(f'Valor total do estoque: R${str(soma)}')
    print('========================================================')
def q2():
    