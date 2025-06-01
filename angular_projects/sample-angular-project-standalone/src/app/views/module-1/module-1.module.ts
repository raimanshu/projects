import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { Module1RoutingModule } from './module-1-routing.module';
import { SharedModule } from '../../shared/shared.module';


@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    Module1RoutingModule,
    // SharedModule
  ]
})
export class Module1Module { }
