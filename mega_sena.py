import random
import time

games = list()
qtd = int(input('Quantos jogos gostaria de sortear? \n'))

for j in range(1, qtd + 1):
    rand = random.sample(range(1, 61), 6)
    rand.sort()
    games.append(rand[:])
    print(f'Jogo {j}: {games[-1]}')
    time.sleep(1)