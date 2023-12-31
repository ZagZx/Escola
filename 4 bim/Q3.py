bib = []

qplat = int(input("Digite a quantidade de prateleiras: "))
qliv = int(input('Digite a quantidade de livros por prateleira: '))
encontrou = False
for a in range(0,qplat):
    bib.append([])
    for b in range(0,qliv):
        bib[a].append('')
while True:
    opcao = int(input('Opções:\n1. Pesquisar livro\n2. Adicionar livro\n3. Remover livro\n4. Imprimir estante\n5. Sair\nEscolha uma opção:'))
    if opcao == 1:
        pesq = input('Qual o nome do livro? ')
        for a in range(0,qplat):
            if pesq in bib[a]:
                print('O livro está na prateleira',a+1)
                print('A posição do livro é',bib[a].index(pesq)+1)
                encontrou == True
        if encontrou == False:
            print('O livro não está na prateleira')
            
    if opcao == 2:
        liv = input('Digite o nome do livro a ser adicionado: ')
        qplat = int(input('Qual a prateleira que está o livro? '))
        oliv = int(input('Qual a posição do livro na prateleira? '))
        bib[qplat-1][oliv -1] = liv
        print('Livro adicionado com sucesso')
    if opcao == 3:
        liv = input('Digite o nome do livro a ser removido: ')
        for o in range(0,qplat):
            for n in bib[o]:
                if n == liv:
                    bib[o][bib[o].index(n)] = ''
    if opcao == 4:
        for i in range(0,qplat):
            print(bib[i])
    if opcao == 5:
        break

        