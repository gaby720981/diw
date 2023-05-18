import { Component } from '@angular/core';

//cada componente tiene un decorador y una clase
@Component({ //decorador, agrega metadatos al componente

  selector: 'app-register', //selector, para acceder desde html.
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})


export class RegisterComponent { //instruccion EXPORT que permite acceder al componente desde afuera.

}
