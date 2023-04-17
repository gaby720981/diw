let form = document.getElementById('formulario');
let mensaje = document.getElementById('mensaje');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  // Obtiene los valores de los campos de entrada
  let nombre = document.getElementById('nombre').value;
  let edad = document.getElementById('edad').value;

  // Actualiza el contenido del elemento "mensaje"
  mensaje.innerHTML = '<p> ¡Hola ' + edad + ' su edad es '+ nombre + '</p>';

  // Muestra el elemento "mensaje"
  mensaje.style.display = 'block';

  // Después de 3 segundos, oculta el elemento "mensaje"
  setTimeout(function() {
    mensaje.style.display = 'none';
  }, 3000);
});
