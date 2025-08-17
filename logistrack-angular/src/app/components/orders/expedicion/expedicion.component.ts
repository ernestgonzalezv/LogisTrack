import { Component } from '@angular/core';

import {OrderStatus} from "../../../../models/enums/order.status";

@Component({
  selector: 'app-expedicion',
  template: `
    <h2>Expedición</h2>
    <app-base-table
      [endpoint]="'orders/distribution'"
      [columnsToShow]="['id', 'pyme_name', 'driver_name', 'dispatch_date', 'bags_count']"
      [statusFilter]="statusExpedition"
      [extraFilters]="expedicionFilters"
    ></app-base-table>
  `
})
export class ExpedicionComponent {
  statusExpedition = OrderStatus.DISPATCHED;

  expedicionFilters = {
    pyme_name: '',
    driver_name: ''
  };
}

