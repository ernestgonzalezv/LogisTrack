import { Component } from '@angular/core';

import {OrderStatus} from "../../../../models/enums/order.status";

@Component({
  selector: 'app-recepcion',
  template: `
    <h2>Recepción</h2>
    <app-base-table
      [endpoint]="'orders/distribution'"
      [columnsToShow]="['pyme_name', 'distribution_center_name', 'dispatch_date', 'incidence_status']"
      [statusFilter]="statusReception"
      [extraFilters]="recepcionFilters"
    ></app-base-table>
  `
})
export class ReceptionComponent {
  statusReception = OrderStatus.RECEIVED;

  recepcionFilters = {
    pyme_name: '',
    distribution_center_name: '',
    incidence_status: ''
  };
}
