import {Component} from "@angular/core";
import {OrderStatus} from "../../../../models/enums/order.status";

@Component({
  selector: 'app-despacho',
  template: `
    <h2>Despacho</h2>
    <app-base-table
      [endpoint]="'orders/distribution'"
      [columnsToShow]="['id', 'pyme_name', 'distribution_center_name', 'dispatch_date']"
      [statusFilter]="statusDispatch"
      [extraFilters]="despachoFilters"
    ></app-base-table>
  `
})
export class DispatchComponent {
  statusDispatch = OrderStatus.PREPARATION;

  despachoFilters = {
    pyme_name: '',
    distribution_center_name: ''
  };
}
