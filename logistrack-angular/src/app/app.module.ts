import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';

// Components
import { DespachoComponent } from './components/orders/despacho/despacho.component';
import { PreparacionComponent } from './components/orders/preparacion/preparacion.component';
import { ExpedicionComponent } from './components/orders/expedicion/expedicion.component';
import { RecepcionComponent } from './components/orders/recepcion/recepcion.component';
import { ConsolidacionComponent } from './components/orders/consolidacion/consolidacion.component';
import { DistribucionComponent } from './components/orders/distribucion/distribucion.component';
import { AsideMenuComponent } from './components/base/aside-menu/aside-menu.component';
import { BaseTableComponent } from './components/base/base-table/base-table.component';

// Angular Material
import { MatTooltipModule } from '@angular/material/tooltip';
import { MaterialModule } from './material-module/material-module.module';
import {MatCardModule} from "@angular/material/card";
import {FormsModule} from "@angular/forms";
import {LoadingTableComponent} from "./components/base/loading-table/loading-table.component";

@NgModule({
  declarations: [
    AppComponent,
    DespachoComponent,
    PreparacionComponent,
    ExpedicionComponent,
    RecepcionComponent,
    ConsolidacionComponent,
    DistribucionComponent,
    AsideMenuComponent,
    BaseTableComponent,
    LoadingTableComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatTooltipModule,
    MaterialModule,
    MatCardModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
