# pegue 4 notas de um aluno (de 0 a 10), calcule a média e diga se foi aprovado ou não(a média do ano precisa ser 6)

nota1 = float(input("Qual é sua primeira nota? "))
while nota1 < -1 or nota1 > 10:
    nota1 = float(input("Digite uma nota válida entre 0 e 10: "))

nota2 = float(input("Qual é sua segunda nota? "))
while nota2 < -1 or nota2 > 10:
    nota2 = float(input("Digite uma nota válida entre 0 e 10: "))

nota3 = float(input("Qual é sua terceira nota? "))
while nota3 < -1 or nota3 > 10:
    nota3 = float(input("Digite uma nota válida entre 0 e 10: "))

nota4 = float(input("Qual é sua quarta nota? "))
while nota4 < -1 or nota4 > 10:
    nota4 = float(input("Digite uma nota válida entre 0 e 10: "))

media = nota1 + nota2 + nota3 + nota4
media = media / 4

notas = [nota1, nota2, nota3, nota4]

print("=========================================")
print("Suas notas são {}".format(notas))
print("A sua média é {}".format(media))

if media == 10:
    media = True

if media is True:
    print("Parabéns, sua nota foi perfeita! Quer um biscoito?")
else:
    if media >= 6:
        print("Você foi aprovado.")
    else:
        print("Você foi reprovado.")
