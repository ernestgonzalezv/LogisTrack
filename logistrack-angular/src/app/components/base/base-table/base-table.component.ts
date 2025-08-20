import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { MatPaginator, PageEvent } from '@angular/material/paginator';
import { MatSort, Sort } from '@angular/material/sort';
import { ApiService } from '../../../services/api.service';


import {Order} from "../../../../models/entities/order";
import {transformOrder} from "../../../../models/mappers/order.mapper";

@Component({
  selector: 'app-base-table',
  templateUrl: './base-table.component.html',
  styleUrls: ['./base-table.component.scss']
})
export class BaseTableComponent implements OnInit {
  @Input() endpoint!: string;
  @Input() statusFilter?: number;
  @Input() extraFilters: Record<string, any> = {};
  @Input() columnsToShow: string[] = [];

  displayedColumns: string[] = [];
  data: any[] = [];
  totalCount = 0;
  filterValue = '';
  pageSize = 20;
  pageIndex = 0;
  sortField = 'id';
  sortDirection: 'asc' | 'desc' = 'asc';
  isLoading: boolean = false;

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(private api: ApiService) {}

  ngOnInit() {
    if (this.columnsToShow.length) {
      this.displayedColumns = [...this.columnsToShow];
    }
    this.loadData();
  }

  extraFilterKeys(): string[] {
    return Object.keys(this.extraFilters);
  }

  applyFilter(event: Event) {
    this.filterValue = (event.target as HTMLInputElement).value;
    this.pageIndex = 0;
    this.loadData();
  }

  clearFilter() {
    this.filterValue = '';
    this.pageIndex = 0;
    this.loadData();
  }

  onPageChange(event: PageEvent) {
    this.pageIndex = event.pageIndex;
    this.pageSize = event.pageSize;
    this.loadData();
  }

  onSortChange(event: Sort) {
    this.sortField = event.active;
    this.sortDirection = event.direction || 'asc';
    this.pageIndex = 0;
    this.loadData();
  }

  getNestedValue(obj: any, path: string) {
    if (!path || !obj) return '';
    return path.split('.').reduce((o, key) => o?.[key], obj) ?? '';
  }

  loadData() {
    this.isLoading = true;
    const filteringOptions: any[] = [{ field: 'search', value: this.filterValue }];
    if (this.statusFilter != null) {
      filteringOptions.push({ field: 'status', value: this.statusFilter.toString() });
    }
    Object.keys(this.extraFilters).forEach(key => {
      const value = this.extraFilters[key];
      if (value !== null && value !== undefined && value !== '') {
        filteringOptions.push({ field: key, value: value.toString() });
      }
    });

    const request = {
      page_args: {
        page_index: this.pageIndex,
        page_size: this.pageSize,
        filtering_options: filteringOptions,
        sorting_options: [{ field: this.sortField, direction: this.sortDirection }]
      }
    };

    this.api.post<any>(this.endpoint, request).subscribe(res => {
      const orders: Order[] = res.data || [];
      const ordersCountMap = new Map<string, number>();
      orders.forEach(o => {
        const blockId = o.block?.id;
        if (blockId) {
          ordersCountMap.set(blockId, (ordersCountMap.get(blockId) ?? 0) + 1);
        }
      });
      this.data = orders.map(o => transformOrder(o, ordersCountMap));


      this.totalCount = res.total_count || this.data.length;
      this.isLoading = false;
    }, () => {
      this.isLoading = false;
    });
  }

  applyExtraFilters() {
    this.pageIndex = 0;
    this.loadData();
  }
}
