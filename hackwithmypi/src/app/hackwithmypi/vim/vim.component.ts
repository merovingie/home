import { Component, OnInit } from '@angular/core';
import { codeTextFieldComponent } from './codeTextField.component';
import { MatDialog } from '@angular/material';

@Component({
  selector: 'app-vim',
  templateUrl: './vim.component.html',
  styleUrls: ['./vim.component.css']
})
export class VimComponent implements OnInit {
  fileName: string;
  codeTextField: string;
  
  constructor(private dialog: MatDialog) { 

   }

  ngOnInit() {
  }
  
  openDialog(): void {
    this.dialog.open(codeTextFieldComponent, {
      width: '550px',
      data: {name: this.fileName, codeTextField: this.codeTextField}
    });
  }

}
