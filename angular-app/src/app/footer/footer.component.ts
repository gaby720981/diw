import { Component } from '@angular/core';

//componente inline si la aplicacion es simple
@Component({

  selector: 'app-footer',
  template: "<p>2023 © copyright  CapacIT - Argentina</p>",
  styles: [ 
    "p{text-align: center; background:  #FFFFFF; padding: 2.5em; font-size: 0.813em; margin: 1.25em; position: absolute; bottom: 0; width: 100%;}", 
  ] 

})   //estilos inline


export class FooterComponent {

}

