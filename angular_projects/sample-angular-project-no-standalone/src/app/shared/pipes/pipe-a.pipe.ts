import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'pipeA',
  standalone:false
})
export class PipeAPipe implements PipeTransform {

  transform(value: unknown, ...args: unknown[]): unknown {
    return null;
  }

}
