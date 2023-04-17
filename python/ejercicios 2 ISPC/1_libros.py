# 1. Definir una clase que represente a Libros, 
# que contenga al menos cinco atributos(variables) que los represente y tres métodos(funciones), 
# de los cuales se necesitará saber: 
# •Cantidad de libros por categoría. 
# •Posibilidad de generar un listado con todos los libros ingresados. 
# •Posibilidad de buscar un libro por nombre y eliminarlo.


class Libros():

    def __init__(self, titulo, autor, paginas, categoria, precio):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas 
        self.categoria = categoria
        self.precio = precio

    def
