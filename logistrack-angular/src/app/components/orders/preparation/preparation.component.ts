import {OrderStatus} from "../../../../models/enums/order.status";
import {Component} from "@angular/core";

@Component({
  selector: 'app-preparacion',
  template: `
    <h2>Preparación</h2>
    <app-base-table
      [endpoint]="'orders/distribution'"
      [columnsToShow]="['id', 'pyme_name', 'preparation_status', 'total_weight', 'total_volume', 'products']"
      [statusFilter]="statusPreparation"
      [extraFilters]="preparacionFilters"
    ></app-base-table>
  `
})
export class PreparationComponent {
  statusPreparation = OrderStatus.PREPARATION;

  preparacionFilters = {
    pyme_name: '',
    preparation_status: ''
  };
}
