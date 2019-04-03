import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MyhistoappComponent } from './myhistoapp/myhistoapp.component';
import { FormsModule } from '@angular/forms';
import { MaterialModule } from './material.module';
import { LoginComponent } from './auth/login/login.component';
import { SignupComponent } from './auth/signup/signup.component';
import { HackwithmypiComponent } from './hackwithmypi/hackwithmypi.component';
import { MrpastaComponent } from './mrpasta/mrpasta.component';
import { CommandsComponent } from './commands/commands.component';
import { WelcomeComponent } from './welcome/welcome.component';


@NgModule({
  declarations: [
    AppComponent,
    MyhistoappComponent,
    LoginComponent,
    SignupComponent,
    HackwithmypiComponent,
    MrpastaComponent,
    CommandsComponent,
    WelcomeComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    BrowserAnimationsModule,
    MaterialModule,
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
