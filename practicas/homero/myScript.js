
function cambiarimg() {
    const img = document.getElementById('img') ;
    const src = img.src ;
    const newSrc = src.endsWith('camaarriba.png') ? 'img/camaabajo.png' : 'img/camaarriba.png' ;
    img.src = newSrc ;
}