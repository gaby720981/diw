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

/*Ámbito 

Javascript habilita tres ámbitos para la declaración de una variable: 

1. Ámbito Global: Cuando se declara una variable fuera de una función, 
está disponible para cualquier otro código en el documento actual. 

2. Ámbito Bloque: variables declaradas con la palabra reservada let / const 
dentro de un bloque de código delimitados por llaves {}, 
esto implica que no pueden ser accesibles fuera de este bloque.*/

