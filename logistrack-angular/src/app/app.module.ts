import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';

// Components
import { DispatchComponent } from './components/orders/dispatch/dispatch.component';
import { PreparationComponent } from './components/orders/preparation/preparation.component';
import { ExpeditionComponent } from './components/orders/expedition/expedition.component';
import { ReceptionComponent } from './components/orders/reception/reception.component';
import { ConsolidationComponent } from './components/orders/consolidation/consolidation.component';
import { DistributionComponent } from './components/orders/distribution/distribution.component';
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
    DispatchComponent,
    PreparationComponent,
    ExpeditionComponent,
    ReceptionComponent,
    ConsolidationComponent,
    DistributionComponent,
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
