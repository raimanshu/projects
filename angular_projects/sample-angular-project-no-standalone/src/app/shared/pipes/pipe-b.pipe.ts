import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'pipeB',
  standalone:false
})
export class PipeBPipe implements PipeTransform {

  transform(value: unknown, ...args: unknown[]): unknown {
    return null;
  }

}
