from random import randint

while True:
    comando = int(input('Digite o número de uma questão: '))

    if comando == 1:
        maior10 = 0
        matriz = [[randint(1,20), randint(1,20), randint(1,20), randint(1,20)],
                  [randint(1,20), randint(1,20), randint(1,20), randint(1,20)],
                  [randint(1,20), randint(1,20), randint(1,20), randint(1,20)],
                  [randint(1,20), randint(1,20), randint(1,20), randint(1,20)]]
        print(matriz[0],'\n',matriz[1],'\n',matriz[2],'\n',matriz[3])
        for a in range(0,4):
            for b in range(0,4):
                if matriz[a][b] > 10:
                    maior10 += 1
        print(f'A matriz tem {maior10} números maiores que 10')
    if comando == 17:
        colunas = 3
        linhas = 10
        matriz = []
        pior1 = 0
        pior2 = 0 
        pior3 = 0
        for a in range(0,linhas):
            matriz.append([])
            for b in range(0,colunas):
                matriz[a].append(randint(0,10))
        
        for c in range(0,linhas):
            if matriz[c][0] < matriz[c][1] and matriz[c][0] < matriz[c][2]:
                pior1 += 1
            elif matriz[c][1] < matriz[c][2]:
                pior2 += 1
            else:
                pior3 += 1
        
        print('\n',pior1,'Alunos tiveram sua pior na 1°','\n',pior2,'Alunos tiveram sua pior na 2°','\n',pior3,'Alunos tiveram sua pior na 3°','\n')        
        for a in range(0,10):
            print(matriz[a])
    if comando == 14:
        matriz = []
        iguais = []
        for a in range(0,5):
            matriz.append([])
            for b in range(0,5):
                aux = randint(0,99)
                while aux in iguais:
                    aux = randint(0,99)
                if aux not in iguais:
                    matriz[a].append(aux)
                    iguais.append(aux)
        
        for a in range(0,5):
            print(matriz[a])
    if comando == 9:
        matriz = []
        
