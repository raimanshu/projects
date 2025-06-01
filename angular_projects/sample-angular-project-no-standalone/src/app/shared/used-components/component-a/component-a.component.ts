import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-component-a',
  standalone:false,
  templateUrl: './component-a.component.html',
  styleUrls: ['./component-a.component.scss']
})
export class ComponentAComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
