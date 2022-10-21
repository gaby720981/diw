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

