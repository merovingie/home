import { Component, OnInit } from '@angular/core';
// import { codeTextFieldComponent } from './codeTextField.component';
import { MatDialog } from '@angular/material';

@Component({
  selector: 'app-vim',
  templateUrl: './vim.component.html',
  styleUrls: ['./vim.component.css']
})
export class VimComponent implements OnInit {
  fileName: string;
  codeArea: string;
  scripts = [{scriptName: 'alpha', scriptContent: 'echo "i love U"'},{ scriptName: 'beta', scriptContent: 'echo "i hate U"'}];
  
  constructor(private dialog: MatDialog) { 

   }

  ngOnInit() {
  }
  
  openDialog(): void {
    this.scripts.push({scriptName: this.fileName, scriptContent: this.codeArea});
    console.log(this.scripts);
  }

}
