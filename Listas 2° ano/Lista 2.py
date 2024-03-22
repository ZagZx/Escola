

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
    feijoes = {
        'feijoada': 0.0,
        'verde': 0.0
    }
    while True:
        venda = input('''
Digite 1 para registrar a venda de um prato de Feijoada 
Digite 2 para registrar a venda de um prato de Feijão Verde

Registrar: ''')
        if venda != '1' or venda !='2':
            break
        else:
            if venda == '1':
                feijoes['feijoada'] += 0.2
                
                
            elif venda =='2':
                feijoes['verde'] += 0.2
            print(f'''
    *********** Consumo de Feijão na Cantina ***********
    Foram consumidos até o momento aproximadamente: 
    * {round(feijoes["feijoada"],2)} quilos de Feijoada
    * {round(feijoes["verde"],2)} quilos de Feijão Verde 
    ****************************************************''')
        
def q3():
    pass