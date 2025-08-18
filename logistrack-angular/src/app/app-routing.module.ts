import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { DispatchComponent } from './components/orders/dispatch/dispatch.component';
import { PreparationComponent } from './components/orders/preparation/preparation.component';
import { ExpeditionComponent } from './components/orders/expedition/expedition.component';
import { ReceptionComponent } from './components/orders/reception/reception.component';
import { ConsolidationComponent } from './components/orders/consolidation/consolidation.component';
import { DistributionComponent } from './components/orders/distribution/distribution.component';

const routes: Routes = [
  { path: '', redirectTo: 'despacho', pathMatch: 'full' },
  { path: 'despacho', component: DispatchComponent },
  { path: 'preparacion', component: PreparationComponent },
  { path: 'expedicion', component: ExpeditionComponent },
  { path: 'recepcion', component: ReceptionComponent },
  { path: 'consolidacion', component: ConsolidationComponent },
  { path: 'distribucion', component: DistributionComponent },

  { path: '**', redirectTo: 'despacho' } // 👈 fallback siempre a despacho
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
