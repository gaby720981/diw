function mensaje() {
    alert("Bienvenido a JS")
}

//OPERADORES ARITMETICOS:

let numero1=10
let numero2=5
console.log(numero1+numero2)
console.log(numero1-numero2)
console.log(numero1*numero2)
console.log(numero1/numero2)
console.log(numero1%numero2) //Resto de la división
console.log(numero1++) //Incremento
console.log(numero1++)
console.log(numero1++)
console.log(numero1--) //Decremento

//DE COMPARACIÓN:
console.log(numero1<=numero2)
console.log(numero1<=numero2)
console.log(numero1!=numero2)
console.log(numero1==numero2)
console.log(numero1<numero2)
console.log(numero1>numero2)

//DE ASIGNACIÓN:
console.log(numero1+=5)//Suma y asignación
console.log(numero1-=5)//Resta y asignación
console.log(numero1*=5)//Producto y asignación
console.log(numero1/=5)//División y asignación
console.log(numero1%=5)//Resto y asignación

//LÓGICOS:
console.log(numero1>numero2 && numero2==6) //AND
console.log(numero1>numero2 || numero2==5) //OR

//VARIABLES - var vs let:
var nnumber = 1 //variable de ámbito global
console.log(number)
{
    var number = "js"
    console.log(number)
}
console.log(number) //toma la última definición

let number2 = 1
console.log(number2)
{
    let number2 = "js"
    console.log(number2)
}
console.log(number2) //Mantiene el primer valor (fuera del bloque)


//TIPOS DE DATOS PRIMITIVOS
//SE ACCEDE DIRECTAMENTE AL VALOR

//STRING
let nombre = "Gaby"
console.log("Mi nombre es", nombre)

//NUMBER
let edad = 30
console.log("Mi edad es", edad)

//BOLEAN
let sabeCantar = true
console.log("Sabe cantar?", sabeCantar)

//NULL
let numerito = null
console.log(numerito)

//UNDEFINED
let apellido
console.log(apellido)

//NAN, no es un número

//CONSTANTES EN TIPO DE DATOS PRIMITIVOS:

const pi = 3.14
let radio = 15
console.log(pi*radio)
