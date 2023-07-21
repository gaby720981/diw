window.sr = ScrollReveal();

// Animación para elementos con la clase "texto1"
sr.reveal('.texto1', {
    duration: 3000,
    origin: 'left', //(izquierda)
    distance: '50px' // Opción para especificar la distancia desde la que se revela el elemento
});

sr.reveal('.texto2', {
    duration: 3000,
    origin: 'right', //(derecha)
    distance: '50px' // Distancia desde el origen
});

sr.reveal('.texto3', {
    duration: 3000,
    origin: 'top', // Animación desde arriba
    distance: '50px'
});
  
  sr.reveal('.texto4, .texto5, .texto6, .texto7, .texto8', {
    duration: 4000,
    origin: 'bottom', // Animación desde abajo
    distance: '50px' 
});

sr.reveal('.img', {
    duration: 5000,
    rotate: {
        x:1,
        y:180,
    }
});
  
  
  
  
  
  
  
  