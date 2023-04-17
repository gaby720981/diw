import random
# ¿Quién comienza?
comienza = random.randint(0, 1)
if comienza == 0:
    print('Comienza el jugador')
else:
    print('Comienza el PC')
# Número aleatorio del parchís
numero = random.randint(1, 6)