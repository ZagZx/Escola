#1. Escrever um algoritmo que lê 5 valores para a, um de cada vez, e conta quantos destes valores são negativos, escrevendo esta informação.

#2. Escrever um algoritmo que lê um valor N inteiro e positivo e que calcula e escreve o valor de E.
#E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / N!

#3. A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
#a) média do salário da população;
#b) média do número de filhos;
#c) maior salário;
#d) percentual de pessoas com salário até R$100,00.

#47. Uma loja tem 150 clientes cadastrados e deseja mandar uma correspondência a cada um deles anunciando um bônus especial.
# Escreva um algoritmo que leia o nome do cliente e o valor das suas compras no ano passado e calcule um bônus de 10% se o valor das compras for
# menor que 500.000 e de15 %, caso contrário.


while True:
    print('Digite o número da questão ou "sair" para fechar o programa')
    ativ = input("Comando: ")
    if ativ == "sair" or ativ == "Sair":
        break

    if ativ == "1":
        negativo1 = 0
        print("======================================")
        for a in range(0,5):
            numero1 = int(input("Digite um número: "))
            if numero1 < 0:
                negativo1 += 1
        if negativo1 == 1:
            print(negativo1, "número é negativo")
        else:
            print (negativo1, "números são negativos")
        print("======================================")

    if ativ == '2':
        print("======================================")
        n2 = int(input("Digite um valor para N: "))
        e2 = 1 + 1 / 1 + 1 / 2 + 1 / 3 + 1 / n2
        print("E = ",e2)
        print("======================================")

    if ativ == "47":
        print("======================================")
        for a in range(0,150):
            nome47 = input("Seu nome: ")
            if nome47 == "sair" or nome47 == "Sair":
                break

            compras47 = float(input("Valor em compras no ano passado: "))
            if compras47 < 500000:
                bonus47 = "10%"
                bonusdin47 = compras47 * (10/100)
            else:
                bonus47 = "15%"
                bonusdin47 = compras47 * (15/100)
            print(f"Olá {nome47}, seu bônus é de {bonus47}, totalizando R${bonusdin47:.2f}")
            print("======================================")
        print("======================================")


