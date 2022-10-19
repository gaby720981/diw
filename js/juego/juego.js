
let puntajeHumano = 0
let puntajeBot = 0

document.querySelector('#piedra').onclick = piedra
document.querySelector('#papel').onclick = papel
document.querySelector('#tijera').onclick = tijera

let humanScore = document.getElementById('human-score')
let botScore = document.getElementById('bot-score')

let estado = document.querySelector('.status')

function rtaBot() {
    let resultado = Math.floor(Math.random() * 3 + 1)
    if (resultado == 1) {
        return 'piedra'
    } else if (resultado == 2) {
        return 'papel'
    } else {
        return 'tijera'
    }
}

function piedra() {
    jugar('piedra')
}

function papel() {
    jugar('papel')
}

function tijera() {
    jugar('tijera')
}

function jugar(humano) {

    let bot = rtaBot()

    if(bot == 'piedra' && humano == 'piedra' || bot == 'papel' && humano == 'papel' || bot == 'tijera' && humano == 'tijera'){
        estado.textContent = `Elegiste ${humano} y el bot eligió ${bot}.
        Es un empate.`
    } else if (bot == 'piedra' && humano == 'papel' || bot == 'papel' && humano == 'tijera' || bot == 'tijera' && humano == 'piedra'){
        estado.textContent = `Elegiste ${humano} y el bot eligió ${bot}.
        ¡Ganaste! :)`
        puntajeHumano++
        humanScore.textContent = `${puntajeHumano}`
    } else if (bot == 'piedra' && humano == 'tijera' || bot == 'papel' && humano == 'piedra' || bot == 'tijera' && humano == 'papel') {
        estado.textContent = `Elegiste ${humano} y el bot eligió ${bot}.
        ¡Perdiste! :(`
        puntajeBot++
        botScore.textContent = `${puntajeBot}`
    } 

}
