import {DistributionCenter} from "./distributionCenter";
import {Block} from "./block";
import {Incidence} from "./incidence";
import {Product} from "./product";
import {Pyme} from "./pyme";

export interface Order {
  id: string;
  pyme: Pyme;
  distribution_center: DistributionCenter;
  dispatch_date: string;
  status: number;
  total_weight: number;
  total_volume: number;
  products: Product[];
  block: Block;
  incidences: Incidence[];
}
