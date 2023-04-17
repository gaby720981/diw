# Tu primer función
# ¿Cómo es que se crea dicha función?

# Se necesita definirla. Aquí, la palabra definir es significativa.

# Así es como se ve la definición más simple de una función:

# def function_name():
#     function_body


# Siempre comienza con la palabra reservada def (que significa definir).
# Después de def va el nombre de la función (las reglas para darle nombre a las funciones son las mismas que para las variables).
# Después del nombre de la función, hay un espacio para un par de paréntesis (ahorita no contienen algo, pero eso cambiará pronto).
# La línea debe de terminar con dos puntos.
# La línea inmediatamente después de def marca el comienzo del cuerpo de la función - donde varias o (al menos una) instrucción anidada será ejecutada cada vez que la función sea invocada; nota: la función termina donde el anidamiento termina, se debe ser cauteloso.

# A continuación se definirá la función. Se llamará message â aquí está:

# def message():
#     print("Ingresa un valor: ")


# La función es muy sencilla, pero completamente utilizable. Se ha nombrado message, pero eso es opcional, tu puedes cambiarlo. Hagamos uso de ella.


# El código ahora contiene la definición de la función:

# def message():
#     print("Ingresa un valor: ")

# print("Se comienza aquí.")
# print("Se termina aquí.")


# Nota: no se está utilizando la función, no se está invocando en el código.

# Al correr el programa, se mostrará lo siguiente:

# Se comienza aquí.
# Se termina aquí.
# salida


# Esto significa que Python lee la definición de la función y la recuerda, pero no la ejecuta sin tu permiso.

# Se ha modificado el código, se ha insertado la invocación de la función entre los dos mensajes:

# def message():
#     print("Ingresa un valor: ")

# print("Se comienza aquí.")
# message()
# print("Se termina aquí.")


# La salida ahora se ve diferente:

# Se comienza aquí.
# Ingresa un valor: 
# Se termina aquí.
# salida


# Prueba el código, modifícalo, experimenta con el.

def my_function():
    # cuerpo de la función