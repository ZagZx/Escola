import sys
def area(lar, com):
    area = largura * comprimento
    print(f"A área do terreno: {largura}m por {comprimento}m é de {area}m²")
def linhas(txt):
    print("~"*len(texto))
    print(texto)
    print("~")


while True:
    print("~"*84)
    comando = input("  Digite o número correspondente do exercício, digite ajuda para mais informações: ")
    print("~" * 84)
    if comando == "ajuda" or comando == "Ajuda":
        print('1 = Exercício de área\n2 = Exercício de linhas\n-Digite "Sair" para fechar o programa')
    if comando == "sair" or comando == "Sair":
        sys.exit("Saindo...")


    if comando == "1":
        largura = int(input("Digite a largura do terreno: "))
        comprimento = int(input("Digite o comprimento do terreno: "))
        area(largura, comprimento)
    if comando == "2":
        texto = input("Digite um texto: ")
        linhas(texto)
