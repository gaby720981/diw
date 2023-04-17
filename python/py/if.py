a=10

if a > 5: print("Es > 5"); print("Dentro del if")

x = 5
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")

x = 5
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")
else:
    print("Es otro")

x = 5
print("Es 5" if x == 5 else "No es 5")


a = 10
b = 5

c = a/b if b!=0 else -1
print(c)

# Verifica si un número es par o impar
x = 6
if not x%2:
    print("Es par")
else:
    print("Es impar")

# Decrementa x en 1 unidad si es mayor que cero
x = 5
x-=1 if x>0 else x
print(x)

