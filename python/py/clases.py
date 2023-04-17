class Perritos: #Creando una clase vacía
    pass

#creamos un objeto de la clase Perritos(instanciar):

mi_perro = Perritos () #dentro de los paréntesis irían los parámetros de entrada

class Perritos:
    #El metodo __init__ es llamado al crear el objeto, reservado para un uso especial del lenguaje
    def __init__ (self, nombre, raza): #SELF:variable que representa la instancia de la clase
        print (f"Creando perrito {nombre}, {raza}.")

        #Atributos de instancia
        self.nombre = nombre
        self.raza = raza

mi_perro = Perritos ("Toby", "Bulldog")
print (type(mi_perro)) #Conocer el tipo de un valor
print (mi_perro.nombre)
print (mi_perro.raza)




class Motovehiculo:
    def __init__  (self, marca, modelo, patente, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente 
        self.kilometraje = kilometraje

moto_negra = Motovehiculo ("Honda", "7698", "GBC342", "3500")

print (moto_negra.patente)
print (moto_negra.marca)


#3.1 EJERCICIO PRACTICO ATRIBUTOS
#agregar año de patentamiento, color, capacidad de tanque.
#cantidad de motos con menos de 1000km, cantidad de motos patentadas en 2021.

class Moto: 
    
    def __init__(self, marca, modelo, patente, kilometraje,añoPatentamiento,color,capacidadTanque ):
        self.Marca = marca
        self.Modelo= modelo
        self.Patente= patente
        self.Kilometraje= kilometraje
        self.AñoPatentamiento= añoPatentamiento
        self.Color= color
        self.CapacidadTanque= capacidadTanque

    def get_Marca(self):
        return self.Marca

    def set_Marca(self, marca):
        self.Marca = marca 
    
    def get_Modelo(self):
        return self.Modelo

    def set_Modelo(self, modelo):
        self.Modelo = modelo

    def get_Patente(self):
        return self.Patente

    def set_Patente(self, patente):
        self.Patente = patente

    def get_Kilometraje(self):
        return self.Kilometraje

    def set_Kilometraje(self, kilometraje):
        self.Kilometraje = kilometraje
    
    def get_Color(self):
        return self.Color

    def set_Color(self, color):
        self.Color = color

    def get_CapacidadTanque(self):
        self.CapacidadTanque

    def set_CapacidadTanque(self, capacidadTanque):
        self.CapacidadTanque= capacidadTanque

    def getAñoPatentamiento(self):
        return self.AñoPatentamiento

    def set_AñoPatentamiento(self,añoPatentamiento):
        self.AñoPatentamiento = añoPatentamiento
 
    def MostrarDatos(self):
        print('La marca de la moto es:' + self.Marca + 
        ' modelo: ' + self.Modelo + 
        'su patente es: '+ self.Patente + 
        'y el kilometraje es: '+ str(self.Kilometraje) +
        'su color es: '+ self.Color + 
        'y el Año de patentamiento  es: ' + str(self.AñoPatentamiento) +
        'la capacidad del tanque es: ' + str(self.CapacidadTanque)
        )
    
    def MotosConMenosDe1000km(self):
        for i in zip(self):
            if(self.kilometraje <1000):
                menos1000km = menos1000km+1
        
        return menos1000km
    
    def Patentes2021(self):
        
        for i in zip(self):
            if(self.añoPatentamiento == 2021):
                patentadasEn2021= patentadasEn2021 + 1
        
        return patentadasEn2021

#5.1 EJERCICIO PRACTICO HERENCIA
#class Triciclomotor:
