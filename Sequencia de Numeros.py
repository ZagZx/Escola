# escreva uma sequência de números e faça com que se você digitar 0, o número anterior será transformado em 0

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

if n2 == 0:
    n1 = n2
if n3 == 0:
    n2 = n3
if n4 == 0:
    n3 = n4

lista = [n1, n2, n3, n4]

print("Sua sequência de números é {}".format(lista))
