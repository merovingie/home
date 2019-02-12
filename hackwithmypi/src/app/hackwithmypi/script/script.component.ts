import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-script',
  templateUrl: './script.component.html',
  styleUrls: ['./script.component.css']
})
export class ScriptComponent implements OnInit {
  panelOpenState = false;
  @Input()
  element: {elementName: string, elementContent: string};
  constructor() { }

  ngOnInit() {
  }

}


