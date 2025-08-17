import {Order} from "./order";

export interface OrdersResponse {
  success: boolean;
  message: string;
  data: Order[];
  page_index: number;
  page_size: number;
  total_count: number;
  total_pages: number;
  has_previous: boolean;
  has_next: boolean;
}
