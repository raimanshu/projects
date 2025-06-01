import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-component-b',
  standalone:false,
  templateUrl: './component-b.component.html',
  styleUrls: ['./component-b.component.scss']
})
export class ComponentBComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
