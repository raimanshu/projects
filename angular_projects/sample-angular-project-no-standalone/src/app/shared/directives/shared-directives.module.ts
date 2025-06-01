import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DirectiveADirective } from './directive-a.directive';
import { DirectiveBDirective } from './directive-b.directive';

const DIRECTIVES = [DirectiveADirective, DirectiveBDirective];

@NgModule({
  declarations: [...DIRECTIVES],
  imports: [CommonModule],
})
export class SharedDirectivesModule {}
