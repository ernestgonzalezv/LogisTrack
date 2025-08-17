import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { DespachoComponent } from './components/orders/despacho/despacho.component';
import { PreparacionComponent } from './components/orders/preparacion/preparacion.component';
import { ExpedicionComponent } from './components/orders/expedicion/expedicion.component';
import { RecepcionComponent } from './components/orders/recepcion/recepcion.component';
import { ConsolidacionComponent } from './components/orders/consolidacion/consolidacion.component';
import { DistribucionComponent } from './components/orders/distribucion/distribucion.component';

const routes: Routes = [
  { path: '', redirectTo: 'despacho', pathMatch: 'full' },
  { path: 'despacho', component: DespachoComponent },
  { path: 'preparacion', component: PreparacionComponent },
  { path: 'expedicion', component: ExpedicionComponent },
  { path: 'recepcion', component: RecepcionComponent },
  { path: 'consolidacion', component: ConsolidacionComponent },
  { path: 'distribucion', component: DistribucionComponent },

  { path: '**', redirectTo: 'despacho' } // 👈 fallback siempre a despacho
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
