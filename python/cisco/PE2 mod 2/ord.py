# Si deseas saber el valor del punto de código ASCII/UNICODE de un carácter específico, 
# puedes usar la función ord() (proveniente de ordinal).

# La función necesita una cadena de un carácter como argumento.
# Incumplir este requisito provoca una excepción TypeError, y devuelve un número que representa el punto de código del argumento.

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))
