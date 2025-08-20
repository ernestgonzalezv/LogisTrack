import { DistributionCenter } from "./distributionCenter";
import { Block } from "./block";
import { Incidence } from "./incidence";
import { Product } from "./product";
import { Pyme } from "./pyme";
import { Reception } from "./reception";

export interface Order {
  id: string;
  pyme: Pyme;
  distribution_center: DistributionCenter;
  dispatch_date: string;
  status: number;
  total_weight: number;
  total_volume: number;
  preparation_status: number;
  distribution_status: number;
  products: Product[];
  block?: Block | null;
  incidences?: Incidence[];
  receptions?: Reception[];
}
