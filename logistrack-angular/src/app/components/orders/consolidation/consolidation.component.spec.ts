import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConsolidationComponent } from './consolidation.component';

describe('ConsolidacionComponent', () => {
  let component: ConsolidationComponent;
  let fixture: ComponentFixture<ConsolidationComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ConsolidationComponent]
    });
    fixture = TestBed.createComponent(ConsolidationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
