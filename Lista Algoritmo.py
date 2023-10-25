while True:
    print('Digite o número da questão ou "sair" para fechar o programa')
    ativ = input("Comando: ")
    if ativ == "sair" or ativ == "Sair":
        break

    if ativ == '1':
        vetor = [1, 0, 5, -2, -5, 7]
        soma = vetor[0] + vetor[1] + vetor[5]
        print("A soma é:",soma)
        vetor[4] = 100
        for a in range(0,6):
            print(vetor[a])

    if ativ == '2':
        vetor = []
        for a in range(0,6):
            vetor.append(int(input("Digite um número: ")))
        print(vetor)
    
    if ativ == '3':
        numeros = []
        quadrados = []
        for a in range(0,10):
            numeros.append(float(input("Digite um número: ")))
        
        for b in range(0,10):
            quadrados.append(numeros[b] * numeros[b])
        print(numeros)
        print(quadrados)
    if ativ == '4':
        vetor = []
        for a in range(0,8):
            vetor.append(int(input('Digite um número: ')))
        pos1 = int(input("Digite uma posição do vetor(de 0 a 7): "))
        pos2 = int(input("Digite outra posição do vetor(de 0 a 7): "))

        soma = vetor[pos1] + vetor[pos2]
        print(soma)
    if ativ == '5':
        vetor = []
        pares = 0
        for a in range(0,10):
            vetor.append(int(input("Digite um número: ")))
        for b in vetor:
            if b % 2 == 0:
                pares += 1
        print(pares)
    if ativ == '6':
        vetor = []
        for a in range(0,10):
            vetor.append(int(input("Digite um número: ")))
        menor = min(vetor)
        maior = max(vetor)
        print(menor)       
        print(maior)
    if ativ == '7':
        vetor = []
        maiorposicao = 0
        for a in range(0,10):
            vetor.append(int(input("Digite um número: ")))
        maior = max(vetor)
        for b in range(0,10):
            if vetor[b] == maior:
                maiorposicao = b
            
        print('Vetor:',vetor)
        print('Maior:',maior)
        print('Posição:',maiorposicao)
    if ativ == '8':
        vetor = []
        for a in range(0,6):
            vetor.append(int(input("Digite um número: ")))
        for b in range(5,-1, -1):
            aux = vetor[b]
            vetor.insert(aux)
            vetor.pop(vetor)
        print(vetor)
    if ativ == '9':
        pares = 0
        lista = []
        while not pares == 6:
            num = int(input('Digite um número par: '))
            if num % 2 == 0:
                lista.insert(0, num)
                pares += 1
        print(lista)
    
    if ativ == '10':
        nota = []
        soma = 0
        for a in range(0,15):
            nota.append(int(input('Digite sua nota: ')))
            soma += nota[a]
        print(nota)
        print('A média da turma é:', soma/15)
    
    if ativ == '11':
        lista = []
        somapos = 0
        qnegativos = 0
        for a in range(0,10):
            lista.append(float(input('Digite um número: ')))
            if lista[a] > 0:
                somapos += lista[a]
            else:
                qnegativos += 1
            
        print(lista)
        print('A soma dos positivos é:',somapos)
        print('A quantidade de negativos é:',qnegativos)
    
    if ativ == '12':
        lista = []
        menor = 99999999999999999999999999999999999999999999
        maior = -9999999999999999999999999999999999999999999
        for a in range(0,5):
            lista.append(int(input('Digite um número: ')))
            if lista[a] > maior:
                maior = lista[a]
            if lista[a] < menor:
                menor = lista[a]
        print(lista)
        print('O maior número é:',maior)
        print('O menor número é:',menor)
    
    if ativ == '13':
        lista = []
        menor = 99999999999999999999999999999999999999999999
        maior = -9999999999999999999999999999999999999999999
        posmenor = -1
        posmaior = -1
        for a in range(0,5):
            lista.append(int(input('Digite um número: ')))
            if lista[a] > maior:
                maior = lista[a]
                posmaior = a
            if lista[a] < menor:
                menor = lista[a]
                posmenor = a

        print(lista)
        print('O maior número está na posição:',posmaior)
        print('O menor número está na posição:',posmenor)
    
    if ativ == '14':
        lista = []
        iguais = []
        for a in range(0,10):
            lista.append(int(input('Digite um número: ')))
        for b in range(0,10):
            for c in range(b+1,10):
                if lista[b] == lista[c] and lista[b] not in iguais:
                    iguais.append(lista[b])         
        print(lista)
        print(iguais)

    if ativ == '15':
        lista = []
        iguaispos = []
        for a in range(0,20):
            lista.append(int(input('Digite um número: ')))
        for a in range(0,20):
            #falta remover os elementos repetidos
            pass
