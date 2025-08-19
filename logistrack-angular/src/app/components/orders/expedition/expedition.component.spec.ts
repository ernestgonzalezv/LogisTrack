import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExpeditionComponent } from './expedition.component';

describe('ExpedicionComponent', () => {
  let component: ExpeditionComponent;
  let fixture: ComponentFixture<ExpeditionComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ExpeditionComponent]
    });
    fixture = TestBed.createComponent(ExpeditionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
