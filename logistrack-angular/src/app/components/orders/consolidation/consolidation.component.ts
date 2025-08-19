import {Component} from '@angular/core';
import {OrderStatus} from "../../../../models/enums/order.status";

@Component({
  selector: 'app-consolidacion',
  template: `
    <h2>Consolidación</h2>
    <app-base-table
      [endpoint]="'orders/distribution'"
      [columnsToShow]="['block_id', 'driver_name', 'orders_count', 'status']"
      [statusFilter]="statusConsolidation"
      [extraFilters]="consolidacionFilters"
    ></app-base-table>
  `
})
export class ConsolidationComponent {
  statusConsolidation = OrderStatus.CONSOLIDATED;

  consolidacionFilters = {
    driver_name: '',
    status: ''
  };
}



