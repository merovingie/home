import { Injectable } from '@angular/core';
import { Commands, ServerReply } from "../models/commands.model";
import { HttpClient, HttpHeaders } from "@angular/common/http"

@Injectable({
  providedIn: 'root'
})
export class TerminalService {

  constructor(private http:HttpClient) { }

  setCommands(commands:any){
    
  }

  getServerReply(){
    return [{
      id: 1,
      replyText: 'xrw------ merovingie:merovingie fake.file',
      alreadyExists: false
    }]
  }
}
