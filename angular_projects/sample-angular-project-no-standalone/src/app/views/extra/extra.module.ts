import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ExtraRoutingModule } from './extra-routing.module';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';


@NgModule({
  declarations: [
    PageNotFoundComponent
  ],
  imports: [
    CommonModule,
    ExtraRoutingModule
  ],
})
export class ExtraModule { }
