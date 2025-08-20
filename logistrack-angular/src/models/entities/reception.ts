import { User } from "./user";

export interface Reception {
  id: string;
  order_id: string;
  user?: User | null;
  reception_date: string;
}

