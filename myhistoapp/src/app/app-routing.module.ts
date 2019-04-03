import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { WelcomeComponent } from './welcome/welcome.component';
import { HackwithmypiComponent } from './hackwithmypi/hackwithmypi.component';
import { CommandsComponent } from './commands/commands.component';
import { SignupComponent } from './auth/signup/signup.component';
import { LoginComponent } from './auth/login/login.component';




const routes: Routes = [
  { path: '', component:WelcomeComponent },
  { path: 'signup', component:SignupComponent },
  { path: 'Login', component:LoginComponent },
  { path: 'hackwithmypi', component:HackwithmypiComponent },
  { path: 'commands', component:CommandsComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
