function cambiarEstado() {
  var numero = document.getElementById("numero").value;
  var estadoSeleccionado = document.getElementById("estado").value;
  var celda = document.querySelector("[data-numero='" + numero + "']");

  if (celda) {
    celda.classList.remove("vendido", "reservado");
    celda.classList.add(estadoSeleccionado);
    estados[numero] = estadoSeleccionado;
  }
}

document.getElementById("reset-button").addEventListener("click", function() {
    // Obtener todas las celdas
    var celdas = document.querySelectorAll("td");

    // Restablecer el estado de todas las celdas a "disponible"
    for (var i = 0; i < celdas.length; i++) {
        celdas[i].classList.remove("reservado");
        celdas[i].classList.remove("vendido");
    }
});

