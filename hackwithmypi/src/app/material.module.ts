import { NgModule } from '@angular/core';
import {MatButtonModule, MatIconModule, MatFormField, MatFormFieldModule, MatInputModule, MatDatepickerModule, MatNativeDateModule, MatCheckboxModule, MatSidenavModule, MatToolbarModule, MatListModule, MatTabsModule,MatCardModule, MatDialogModule, MatExpansionModule} from '@angular/material';

@NgModule({
    imports: [ MatButtonModule, MatIconModule ,MatFormFieldModule, MatInputModule, MatDatepickerModule, MatNativeDateModule, MatCheckboxModule, MatSidenavModule, MatToolbarModule, MatListModule, MatTabsModule,MatCardModule, MatDialogModule, MatExpansionModule ],
    exports: [ MatButtonModule, MatIconModule ,MatFormFieldModule, MatInputModule, MatDatepickerModule, MatNativeDateModule, MatCheckboxModule, MatSidenavModule, MatToolbarModule, MatListModule, MatTabsModule,MatCardModule, MatDialogModule, MatExpansionModule ]
})
export class MaterialModule {}