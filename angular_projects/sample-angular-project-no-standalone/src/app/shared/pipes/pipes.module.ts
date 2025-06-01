import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PipeAPipe } from './pipe-a.pipe';
import { PipeBPipe } from './pipe-b.pipe';

const PIPES = [PipeAPipe, PipeBPipe];

@NgModule({
  declarations: [...PIPES],
  imports: [
    CommonModule
  ]
})
export class PipesModule { }
