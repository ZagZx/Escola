comando = input('Digite o número da questão: ')
print()


if comando == '1':
    print('Janeiro\nFevereiro\nMarço\nAbril\nMaio\nJunho\nJulho\nAgosto\nSetembro\nOutubro\nNovembro\nDezembro')
if comando == '1.1':
    lista = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    for a in lista:
        print(a)

if comando == "2":
    var = ''
    for a in range(1,10):
        if a != 9:
            var += f'{a}, '
        else:
            var += f"{a}"
    print(var)
if comando == '3':
    print('''
        *****
        *   *
        *   *
        *   *
        *****   
          ''')
if comando == '3.1':
    for a in range(1,6):
        if a == 1 or a == 5:
            print('*'*5)
        else:
            print('*   *')