import {Component} from "@angular/core";
import {OrderStatus} from "../../../../models/enums/order.status";

@Component({
  selector: 'app-preparacion',
  template: `
    <h2>Preparación</h2>
    <app-base-table
      [endpoint]="'orders/distribution'"
      [columnsToShow]="['id', 'pyme_name', 'status', 'total_weight', 'total_volume', 'products']"
      [statusFilter]="statusPreparation"
      [extraFilters]="preparacionFilters"
    ></app-base-table>
  `
})
export class PreparacionComponent {
  statusPreparation = OrderStatus.PREPARATION;

  preparacionFilters = {
    pyme_name: '',
    status: ''
  };
}
