alfabeto = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lista = []
palavra = []
palavratraduz = ''
while True:
    aux = int(input('Posição da letra no alfabeto: '))
    if aux < 0:
        break
    if aux > 27:
        break
    lista.append(aux)

for a in range(0,len(lista)):
    palavra.append(alfabeto[lista[a]])
    palavratraduz += palavra[a]

print('Palavra Traduzida:',palavratraduz)
print('Posições no alfabeto:',lista)