import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { FormsModule } from '@angular/forms';
import { MaterialModule } from './material.module';
import { loginComponent } from './auth/login/login.component';
import { SignupComponent } from './auth/signup/signup.component';
import { HackwithmypiComponent } from './hackwithmypi/hackwithmypi.component';
import { MrpastaComponent } from './mrpasta/mrpasta.component';
import { CommandsComponent } from './commands/commands.component';
import { WelcomeComponent } from './welcome/welcome.component';
import {FlexLayoutModule} from '@angular/flex-layout';
import { VimComponent } from './hackwithmypi/vim/vim.component';
import { TerminalComponent } from './hackwithmypi/terminal/terminal.component';
// import { codeTextFieldComponent } from './hackwithmypi/vim/codeTextField.component';
import { ScriptComponent } from './hackwithmypi/script/script.component';
import { HttpClientModule } from "@angular/common/http";

@NgModule({
  declarations: [
    AppComponent,
    WelcomeComponent,
    CommandsComponent,
    MrpastaComponent,
    SignupComponent,
    loginComponent,
    HackwithmypiComponent,
    VimComponent,
    TerminalComponent,
    ScriptComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    BrowserAnimationsModule,
    MaterialModule,
    FlexLayoutModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent],
  entryComponents: []
})
export class AppModule { }
