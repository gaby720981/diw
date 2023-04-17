for i in range(0, 5):
    print(i)

for i in "Python":
    print(i)

lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]

for i in lista:
    print(i)
#[56, 34, 1]
#[12, 4, 5]
#[9, 4, 3]

for i in lista:
    for j in i:
        print(j)
# Salida: 56,34,1,12,4,5,9,4,3


for i in range(6):
    print(i)

#range(inicio, fin, salto)
for i in range(5, 20, 2):
    print(i) #5,7,9,11,13,15,17,19

x = 5
while x > 0:
    x -=1
    print(x)

#ó:
x = 5
while x > 0: x-=1; print(x)

x = ["Uno", "Dos", "Tres"]
while x:
    x.pop(0)
    print(x)

# Permutación a generar
i = 0
j = 0
while i < 3:
    while j < 3:
        print(i,j)
        j += 1
    i += 1
    j = 0

#árbol de navidad

z = 7
x = 1
while z > 0:
    print(' ' * z + '*' * x + ' ' * z)
    x+=2
    z-=1


cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break
    print(letra)


x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
    print("Fin del bucle")


cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        continue
    print(letra)
