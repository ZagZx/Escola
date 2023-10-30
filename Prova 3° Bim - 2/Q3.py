palavra = input('Digite uma palavra: ')
vogais = ['a','e','i','o','u']
vogaismaiusculas = ['A','E','I','O','U']
vogaispalavra = []
consoantespalavra = []
novapalavra = ''

for letra in palavra:
    if letra in vogais:
        vogaispalavra.append(letra)
        novapalavra += vogaismaiusculas[vogais.index(letra)]
    else:
        if letra != ' ':
            consoantespalavra.append(letra)
        novapalavra += letra

print()
print(f'A palavra {palavra} contém {len(vogaispalavra)} vogais e {len(consoantespalavra)} consoantes')
print('Nova String:', novapalavra)
print()
print('Vogais na palavra:',vogaispalavra)
print()
print('Consoantes na palavra:',consoantespalavra)
