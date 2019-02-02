import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MyhistoappComponent } from './myhistoapp.component';

describe('MyhistoappComponent', () => {
  let component: MyhistoappComponent;
  let fixture: ComponentFixture<MyhistoappComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MyhistoappComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MyhistoappComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
