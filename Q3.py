palavra = input('Digite uma palavra: ')
vogais = ['a','e','i','o','u']
vogaismaiusculas = ['A','E','I','O','U']
vogaispalavra = []
consoantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
consoantespalavra = []


for a in vogais:
    if a in palavra:
        vogaispalavra.append(a)
for b in consoantes:
    if b in palavra:
        consoantespalavra.append(b)

print()
print(f'A palavra {palavra} contém {len(vogaispalavra)} vogais e {len(consoantespalavra)} consoantes')
print('Nova String:', palavra.replace('a','A').replace('e','E').replace('i','I').replace('o','O').replace('u','U'))
print()
print('Vogais na palavra:',vogaispalavra)
print()
print('Consoantes na palavra:',consoantespalavra)

