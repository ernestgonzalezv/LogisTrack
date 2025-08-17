import { Component } from '@angular/core';

import {OrderStatus} from "../../../../models/enums/order.status";

@Component({
  selector: 'app-distribucion',
  template: `
    <h2>Distribución</h2>
    <app-base-table
      [endpoint]="'orders/distribution'"
      [columnsToShow]="['id', 'driver_name', 'dispatch_date', 'status']"
      [statusFilter]="statusDistribution"
      [extraFilters]="distribucionFilters"
    ></app-base-table>
  `
})
export class DistribucionComponent {
  statusDistribution = OrderStatus.DELIVERED;

  distribucionFilters = {
    driver_name: '',
    status: ''
  };
}

