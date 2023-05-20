import { Component } from '@angular/core';
import { EmpleadosService } from './services/empleados.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})



export class AppComponent {
  title = 'angular-app';


  constructor(private miServicio:EmpleadosService) {}
}
