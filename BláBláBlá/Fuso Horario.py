import sys
print("="*35)
hemisferios = int(input("Digite 0 para hemisférios iguais e 1 para hemisférios diferentes: "))
print("="*35)
while hemisferios < 0 or hemisferios > 1:
    hemisferios = int(input("Digite um número entre 0 e 1: "))

if hemisferios == 0:
    longitudea = int(input("Digite a longitude do ponto A: "))
    horasa = float(input("Que horas são no ponto A? "))
    longitudeb = int(input("Digite a longitude do ponto B: "))

    calculo = longitudea - longitudeb

    if calculo >= 0:
        horasb = calculo / 15 + horasa
        diferenca = calculo / 15
        if horasb > 24:
            horasb = horasb - 24
        if horasa > 0:
            horasb = calculo / 15 + horasa
            if horasb > 24:
                horasb = horasb - 24
        if horasb == 24:
            horasb = 0

        if 0 < horasb < 10:
            print("="*35)
            print("A diferença de horário é de {:.2f} horas".format(diferenca))
            print("No ponto B são 0{:.2f} horas".format(horasb))
            sys.exit()
        if horasb >= 10:
            print("=" * 35)
            print("A diferença de horário é de {:.2f} horas".format(diferenca))
            print("No ponto B são {:.2f} horas".format(horasb))
            sys.exit()
        if horasb == 0:  # bug do 0 negativo
            print("=" * 35)
            horasb = horasb * -1
            print("A diferença de horário é de {:.2f} horas".format(diferenca))
            print("No ponto B são 0{:.2f} horas".format(horasb))
            sys.exit()

    if calculo < 0:
        calculo = calculo * -1
        horasb = calculo / 15 - horasa
        horasb = horasb * -1
        diferenca = calculo / 15
        if horasa == 0:
            horasb = horasb + 24
        if 0 < horasa < 1:  # caso seja 00:30, por exemplo
            horasb = horasb + 24
        if horasb == 24:
            horasb = 0

        if horasb == 0:  # bug do 0 negativo
            horasb = horasb * -1
            print("=" * 35)
            print("A diferença de horário é de {:.2f} horas".format(diferenca))
            print("No ponto B são 0{:.2f} horas".format(horasb))
            sys.exit()
        if horasb >= 10:
            print("=" * 35)
            print("A diferença de horário é de {:.2f} horas".format(diferenca))
            print("No ponto B são {:.2f} horas".format(horasb))
            sys.exit()
        if 0 < horasb < 10:
            print("=" * 35)
            print("A diferença de horário é de {:.2f} horas".format(diferenca))
            print("No ponto B são 0{:.2f} horas".format(horasb))
            sys.exit()


if hemisferios == 1:
    longitudea = int(input("Digite a longitude do ponto A: "))
    horasa = float(input("Que horas são no ponto A? "))
    longitudeb = int(input("Digite a longitude do ponto B: "))

    calculo = longitudea + longitudeb
    horasb = calculo / 15 + horasa
    diferenca = calculo / 15
    if horasb == 0:
        horasb = horasb - 12
    if horasb == 24:
        horasb = 0
    if horasb > 24:
        horasb = horasb - 24

    if horasb == 0 or 0 < horasb < 1:
        print("=" * 35)
        print("A diferença de horário é de {:.2f} horas".format(diferenca))
        print("No ponto B são 0{:.2f} horas".format(horasb))
    if horasb != 0:
        print("=" * 35)
        print("A diferença de horário é de {:.2f} horas".format(diferenca))
        print("No ponto B são {:.2f} horas".format(horasb))
