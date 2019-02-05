import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MrpastaComponent } from './mrpasta.component';

describe('MrpastaComponent', () => {
  let component: MrpastaComponent;
  let fixture: ComponentFixture<MrpastaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MrpastaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MrpastaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
