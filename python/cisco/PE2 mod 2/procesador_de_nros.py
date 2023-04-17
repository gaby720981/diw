#permite ingresar una línea llena de números y sumarlos fácilmente

#Procesador de Números.

line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")

# La línea 03: pide al usuario que ingrese una línea llena de cualquier cantidad de números (los números pueden ser flotantes).
# La línea 04: divide la línea en una lista con subcadenas.
# La línea 05: se inicializa la suma total a cero.
# La línea 06: como la conversión de cadena a flotante puede generar una excepción, es mejor continuar con la protección del bloque try-except.
# La línea 07: itera a través de la lista...
# La línea 08: ... e intenta convertir todos sus elementos en números flotantes; si funciona, aumenta la suma.
# La línea 09: todo está bien hasta ahora, así que imprime la suma.
# La línea 10: el programa termina aquí en caso de error.
# La línea 11: imprime un mensaje de diagnóstico que muestra al usuario el motivo de la falla.