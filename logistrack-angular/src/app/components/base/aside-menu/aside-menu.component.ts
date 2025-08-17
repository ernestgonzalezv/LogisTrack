// src/app/components/aside-menu/aside-menu.component.ts
import { Component } from '@angular/core';
import {MaterialModule} from "../../../material-module/material-module.module";
import {RouterLink, RouterLinkActive, RouterOutlet} from "@angular/router";

interface MenuItem {
  name: string;
  route: string;
  icon: string;
}

@Component({
  selector: 'app-aside-menu',
  templateUrl: './aside-menu.component.html',
  styleUrls: ['./aside-menu.component.scss']
})
export class AsideMenuComponent {
  menuItems: MenuItem[] = [
    { name: 'Despacho', route: '/despacho', icon: 'local_shipping' },
    { name: 'Preparación', route: '/preparacion', icon: 'inventory' },
    { name: 'Expedición', route: '/expedicion', icon: 'flight_takeoff' },
    { name: 'Recepción', route: '/recepcion', icon: 'move_to_inbox' },
    { name: 'Consolidación', route: '/consolidacion', icon: 'layers' },
    { name: 'Distribución', route: '/distribucion', icon: 'delivery_dining' },
  ];
}
