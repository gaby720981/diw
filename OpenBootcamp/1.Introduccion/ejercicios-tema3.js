//(04/05/23) 

//Primera parte:
// Crear una función con tres parámetros que sean números que se suman entre sí.
// Llamar a la función en el main y darle valores.

// Segunda parte:
// Crear una clase coche.
// Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
// Una función que incremente el número de puertas que tiene el coche.
// Crear un objeto miCoche en el main y añadirle una puerta.
// Mostrar el número de puertas que tiene el objeto.

//Función para sumar tres números
function sumaTresNumeros (num1, num2, num3) {
    return num1 + num2 + num3;
}

//Llamada a la función con valores
console.log(sumaTresNumeros(3, 5, 7));

//Clase Coche
class Coche {
    constructor(numPuertas){
        this.numPuertas = numPuertas;
    }
    //Función para incrementar número de puertas
    agregarPuerta () {
        this.numPuertas++;
    }
}

//Creación objeto coche y añadiendo una puerta
let miCoche = new Coche (4);
miCoche.agregarPuerta();

//Mostrando el número de puertas del objeto
console.log(miCoche.numPuertas);