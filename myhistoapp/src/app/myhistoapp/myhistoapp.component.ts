import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-myhistoapp',
  templateUrl: './myhistoapp.component.html',
  styleUrls: ['./myhistoapp.component.scss']
})
export class MyhistoappComponent implements OnInit {
  @Input() firstname: string;
  @Input() lastname: string;
  @Input() height: number;
  helloString: string = "why You WHYYYYYYY what Should i do when math exam is a shoe";
  Zcolor:string="text-danger";
  allowButton = false;
  date = new Date(2000, 3, 1)
  newAddTodo = ""
  Todos:Array<string> = []
  allowList:boolean = false
  allowFinished: boolean = true
  
  constructor() { }

  ngOnInit() {
  }
  
  get string_trunc(){
    return this.helloString.slice(0,5);
  }
  get height_feet(){
    return this.height * 0.328;
  }

  height_up(){
    this.height += 1;
  }

  height_down(){
    this.height -= 1;
  }

  turnTextColorGreen(){
    this.Zcolor = "text-info";
  }
  
  allowButtonButton(){
    setTimeout(() => {
      this.allowButton = true;
    }, 5000);
  }
  
  onUpdate(event:any){
    this.newAddTodo = event.target.value;
    console.log(this.newAddTodo);
  }

  addTolist(){
    this.allowList = true
    this.Todos.push(this.newAddTodo)
    console.log(this.Todos)
  }

  ondeleteTodo(Todo:string){
    const index = this.Todos.indexOf(Todo, 0)
    console.log(index)
    if ( index > -1){
    this.Todos.splice(index, 1);
    }
  }

  onfinished(Todo){
    this.allowFinished = false;
  }
}
