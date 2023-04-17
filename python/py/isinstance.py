# La isinstance()función devuelve True si el objeto especificado es del tipo especificado, de lo contrario False.

# Si el parámetro de tipo es una tupla, esta función devolverá Truesi el objeto es uno de los tipos de la tupla.

isinstance(object, type)

x = isinstance(5, int)

x = isinstance("Hello", (float, int, str, list, dict, tuple))

