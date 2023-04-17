first_number = int(input("Ingresa el primer numero: "))
second_number = int(input("Ingresa el segundo numero: "))

try:
    print(first_number / second_number)
except:
    print("Esta operación no puede ser realizada.")

print("FIN.")

# La palabra reservada try comienza con un bloque de código el cual puede o no estar funcionando correctamente.
# Después, Python intenta realizar la acción arriesgada: si falla, se genera una excepción y Python comienza a buscar una solución.
# La palabra reservada except comienza con un bloque de código que será ejecutado si algo dentro del bloque try sale mal: 
# si se genera una excepción dentro del bloque anterior try, fallará aquí, entonces el código ubicado después de 
# la palabra clave reservada except debería proporcionar una reacción adecuada a la excepción planteada.
# Por ultimo, se regresa al nivel de anidación anterior, es decir, se termina la sección try-except.

try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salió mal...")

print("FIN.")


try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh cielos, algo salió mal...")

print("3")


# No olvides que:

# Los bloques except son analizados en el mismo orden en que aparecen en el código.
# No debes usar más de un bloque de excepción con el mismo nombre.
# El número de diferentes bloques except es arbitrario, la única condición es que si se emplea el try, 
# debes poner al menos un except (nombrado o no) después de el.
# La palabra clave reservada except no debe ser empleada sin que le preceda un try.
# Si uno de los bloques except es ejecutado, ningún otro lo será.
# Si ninguno de los bloques except especificados coincide con la excepción planteada, 
# la excepción permanece sin manejar (lo discutiremos pronto).
# Si un except sin nombre existe, tiene que especificarse como el último.

# try:
#     :
# except exc1:
#     :
# except exc2:
#     :
# except:
#     :


        