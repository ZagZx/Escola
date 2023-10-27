tamanho = int(input('Tamanho das listas: '))

print('='*30)

lista = []
lista2 = []
iguais = []

for l1 in range(0,tamanho):
    lista.append(int(input(f'Digite o {l1+1}º elemento da lista 1: ')))
print('='*30)
for l2 in range(0,tamanho):
    lista2.append(int(input(f'Digite o {l2+1}º elemento da lista 2: ')))

for a in lista:
    for b in lista2:
        if a == b and a not in iguais:
            iguais.append(a)

#nas seguintes linhas dava para ter feito só um print mas eu decidi enfeitar arrumando o plural e singular

if len(iguais) == 1:
    print('O número que se repete é:', iguais)
else:
    print('O números que se repetem são:', iguais)
