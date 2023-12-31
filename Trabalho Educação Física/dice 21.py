import random

soma = 0
players = []
dados = []

for a in range(1,5):
    players.append(input(f'Player {a}: '))
    dados.append(random.randint(1,6))

print(players)
print(dados)

while soma != 21:
    comando = input('Girar ou parar?')
