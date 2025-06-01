import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { ForgetComponent } from './forget/forget.component';
import { RegisterComponent } from './register/register.component';

const routes: Routes = [
  {path:"login", 
    loadComponent: ()=> import('./login/login.component').then(m => LoginComponent)
  },
    {path:"forget-password", 
    loadComponent: ()=> import('./forget/forget.component').then(m => ForgetComponent)
  },
    {path:"register", 
    loadComponent: ()=> import('./register/register.component').then(m => RegisterComponent)
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AuthRoutingModule { }
