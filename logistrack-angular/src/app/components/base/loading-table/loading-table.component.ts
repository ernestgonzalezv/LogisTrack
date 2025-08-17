import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-loading-table',
  templateUrl: './loading-table.component.html',
})
export class LoadingTableComponent {
  @Input() loading: boolean = false;
}
