class Perro:
    #constructor
    def __init__(self):
        self.nombre =None
        self.tamaño = None
        self.edad = 0
        self.color = None
        self.raza = None

    #metodos
    def ladrar(self):
        print("El perro ladra")
    
    def comer(self):
        print("El perro come")

    def jugar(self):
        print("El perro juega")
    
    #setter // getter
    def cambiar_nombre(self,nombre):
        self.nombre = nombre
        print("El perro ahora se llama{}".format(nombre))
    
    def set_edad(self,edad):
        self.edad =edad
        print("{} ahora tiene {} añños".format(self.nombre,self.edad))
    
    def cumpleaños(self):
        self.edad += 1
        print("{} ahora tiene {} añños".format(self.nombre,self.edad))
    
#instanciar un objeto
mi_perro = Perro()
print(mi_perro)
mi_perro.comer
print(mi_perro.raza)
mi_perro.cambiar_nombre("Tomy")
print(mi_perro.nombre) 