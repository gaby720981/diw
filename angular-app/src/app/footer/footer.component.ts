import { Component } from '@angular/core';

//componente inline si la aplicacion es simple
@Component({

  selector: 'app-footer',
  template: "<p>2023 © copyright  CapacIT - Argentina</p>",
  styles: [
    "p{text-align: center; padding: 2em; margin: 1em; position: absolute; bottom: 0; width: 90%;}",
  ]

})   //estilos inline


export class FooterComponent {

}

