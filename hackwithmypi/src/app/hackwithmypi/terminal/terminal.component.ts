import { Component, OnInit } from '@angular/core';
import { Commands, ServerReply } from '../../models/commands.model';
import { NgForm } from '@angular/forms';
import { TerminalService } from "../../services/terminal.service";
import { all } from 'q';


@Component({
  selector: 'app-terminal',
  templateUrl: './terminal.component.html',
  styleUrls: ['./terminal.component.css']
})
export class TerminalComponent implements OnInit {
  commandsText = '';
  serverReplyText = '';
  serverReply:ServerReply[];
  commands:Commands[];


  
  constructor(private terminalService:TerminalService) { }

  ngOnInit() {
    console.log("on Init initialized")
  }
  commandRegex(com: string):Commands{
   return  
      
   
  }

  onPostCommand(form: NgForm){
    console.log(form);
    this.commandsText = form.value.terminal;
    //this.commands.push(this.commandRegex(this.commandsText));
    //console.log(this.commands);
    console.log(this.commandsText);
    this.serverReply = this.terminalService.getServerReply();
    //this.terminalService.setCommands(this.commands);
    this.serverReplyText = this.serverReply[0].replyText;
    console.log(this.serverReply);
    console.log(this.serverReplyText);
  }
}
