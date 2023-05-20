import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegisterComponent } from './register/register.component';
import { EmpleadosComponent } from './empleados/empleados.component';
import { EmpleadoComponent } from './empleado/empleado.component';
import { FooterComponent } from './footer/footer.component';
import { EmpleadosService } from './services/empleados.service';



@NgModule({ //aqui deben estar declarados todos los componentes
  declarations: [
    AppComponent,
    RegisterComponent,
    EmpleadosComponent,
    EmpleadoComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [EmpleadosService],
  bootstrap: [AppComponent]
})
export class AppModule { }

