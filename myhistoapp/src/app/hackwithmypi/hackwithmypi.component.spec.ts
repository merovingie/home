import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HackwithmypiComponent } from './hackwithmypi.component';

describe('HackwithmypiComponent', () => {
  let component: HackwithmypiComponent;
  let fixture: ComponentFixture<HackwithmypiComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HackwithmypiComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HackwithmypiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
