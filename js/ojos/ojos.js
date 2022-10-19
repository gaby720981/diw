document.querySelector('body').addEventListener('mousemove', pupila)



function pupila() {

    const ojo = document.querySelectorAll('.ojo')
    
    ojo.forEach(function(ojo) {

        let x = (ojo.getBoundingClientRect().left) + (ojo.clientWidth / 2)
        let y = (ojo.getBoundingClientRect().top) + (ojo.clientHeight / 2)

        let radio = Math.atan2(event.pageX - x, event.pageY - y)
        let rotacion = (radio * (180 / Math.PI) * -1) + 270

        ojo.style.transform = "rotate("+rotacion+"deg)"

    })

    

}


// elemento.getBoundingClientRect() -> devuelve el tamaño del elemento y su posicion relativa
// respecto al viewport. Devuelve un valor fraccional

// element.clientWidth -> par elementos sin CSS es 0. En caso contrario, es la anchura interior
// de un elemento en píxeles incluyendo el padding. Devuelve un entero

// Math.atan2 -> retorna la arcotangente del cociente de los argumentos

// arcotangente -> función inversa de la tangente de un angulo
// tangente -> es una recta que toca a la curva solo en dicho punto (punto de tangencia)