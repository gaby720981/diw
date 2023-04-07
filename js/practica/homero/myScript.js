


function cambiarimg() {
    const img = document.getElementById('img') ;
    const src = img.src ;
    const newSrc = src.endsWith('camaarriba.jpg') ? 'img/camaabajo.jpg' : 'img/camaarriba.jpg' ;
    img.src = newSrc ;
}