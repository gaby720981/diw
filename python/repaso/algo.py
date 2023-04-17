lenguaje = "Python"

if lenguaje == "Python":
    print ("Estoy de acuerdo, Python es el mejor")
elif lenguaje == "Java":
    print ("No me gusta, Java no mola")
else:
    print ("Ningún otro lenguaje supera a Python")


x = 0
while x < 3:
    print (x)
    x += 1         # x = x + 1

print ("***********************")

for i in range (3):
    print(i)

print ("***********************")

for i in range(3):
    if i == 1:
        continue
    print(i)

print ("***********************")

for i in range(8):
    if i == 5:
        break
    print(i)

print ("***********************")

x = 0
while True:
    print (x)
    x += 1
    if x == 5:
        break

print ("***********************")

def funcion_suma (a,b):
    return a + b

suma = funcion_suma (4,8)
print ("La suma es", suma)

def generador():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

for i in generador():
    print(i)


class MiClase:
    def __init__(self):
        print ("Creando objeto de MiClase")

objeto = MiClase()


X = "10"

valor = None
try:
    valor = int(x)
except Exception as e:
    print("Hubo un error:", e)
finally:
    print("El valor es", valor)


    
v= 1 + (1 // 2) + (1 / 2) + 2
print (v)
t = 1 // 2
p = 1 / 2
print (t)
print (p)