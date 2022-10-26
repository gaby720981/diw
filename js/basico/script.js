function nombre() {
    nombre = prompt("Cuál es tu nombre?")
    alert("¡Hola " + nombre + "!")
}

function edad() {
    edad = prompt ("Bienvenido al Club Nocturno 'Xxxx'. Qué edad tienes?")
    edad = parseInt (edad)
    if (edad < 18) {
        alert ("No podés pasar, lo siento...")
    }
    else {
        alert ("Podés pasar. ¡Que disfrutes!")
    }
}

function mostrarMensaje() {
    alert ("Bienvenido")
}

/*Esto es un comentario 
multilínea*/

// Esto es un comentario de una sola línea

//Ejemplo de declaración y asignación de valor: 

var mi_dato_numerico = 3; 
var mi_dato_texto = "hola";

//Un identificador tiene que empezar con una letra, un guion bajo (_) o un símbolo de dólar ($).

var _numero = 100; //VAR declara una variable, inicializándola opcionalmente a un valor.
var numero = 100; 
let $numero = 100; //LET declara una variable local en un bloque de ámbito (scope), inicializándola opcionalmente a un valor.
const numeroPar = 100; 
const PI = 3.14; /*CONST declara una constante de sólo lectura en un bloque de ámbito. 
Funciona como una variable pero no cambia su valor, es decir, representa un lugar de 
almacenamiento de tipos de datos en la memoria pero una vez asignado el valor inicial 
no puede ser modificado.*/


/*Ámbitos para la declaración de una variable: 

1. Ámbito Global: Cuando se declara una variable fuera de una función, 
está disponible para cualquier otro código en el documento actual. 

2. Ámbito Bloque: Variables declaradas con la palabra reservada let / const 
dentro de un bloque de código delimitados por llaves {}, 
esto implica que no pueden ser accesibles fuera de este bloque.

3. Ámbito Función: Se le denomina variable local, porque está disponible sólo dentro de esa función.

/*OPERADOR CONDICIONAL (TERNARIO): 

Necesita tres operadores.
El operador asigna uno de dos valores basado en una condición. 
La sintaxis de este operador es: condición? valor1: valor2. 
Si la condición es verdadera, el operador tomará el valor 1, de lo contrario tomará el valor 2. 
Se puede usar el operador condicional en cualquier lugar que use un operador estándar. 
Ejemplo: esta sentencia asigna el valor adulto a la variable estado si la edad es mayor o igual a 18, 
de lo contrario le asigna el valor menor: 
    
var estado = (edad>= 18)? "adulto": "menor";

/*FUNCIONES

función nombre (parámetro1, parámetro2) {
     // código ha ser ejecutado; 
}
    
CICLOS

for ([expresion-inicial]; [condicion]; [expresion-final]) { 
    // código ha ser ejecutado; 
}

for (var i = 0; 1 <10; i ++) {
    console.log ("Número:" + i); 
}
    
while ([condicion]) { 
    // código ha ser ejecutado; 
}

DO-WHILE: Se utiliza para repetir instrucciones un número indefinido de veces, hasta que se cumpla una condición.

let resultado = ''; 
let i = 0; 
do { 
    i = i + 1; resultado = resultado + i; 
} 
while (i <5); 
console.log (resultado);

// resultado esperado: "12345"

CONTINUE:

do { 
    i = i + 1; 
    continue; 
} while (i <5);

BREAK:

do { 
    i = i + 1; 
    if (i == 3) 
    break; 
} while (i <5);

    */

