import { Order } from "../entities/order";
import { getStatusText } from "../enums/order.status";
import { getIncidenceStatusText } from "../enums/incidence.status";
import { getPreparationStatusText } from "../enums/preparation.status";
import { getDistributionStatusText } from "../enums/distribution.status";

export function transformOrder(order: Order, ordersCountMap: Map<string, number>): Record<string, any> {
  const blockId = order.block?.id;
  const ordersCount = blockId ? (ordersCountMap.get(blockId) ?? 1) : 0;

  // Mapea solo las propiedades que quieres mostrar en la tabla
  return {
    id: order.id ?? 'Inexistente',
    pyme_name: order.pyme?.name ?? 'Inexistente',
    distribution_center_name: order.distribution_center?.name ?? 'Inexistente',
    dispatch_date: order.dispatch_date ? formatDate(order.dispatch_date) : 'Inexistente',
    preparation_status: getPreparationStatusText(order.preparation_status), // <-- aquí
    distribution_status: getDistributionStatusText(order.distribution_status),
    total_weight: order.total_weight ?? 0,
    total_volume: order.total_volume ?? 0,
    products: order.products?.length ? order.products.map(p => p.name).join(', ') : 'Inexistente',
    driver_name: order.block?.driver?.name ?? 'Inexistente',
    driver_phone: order.block?.driver?.phone ?? 'Inexistente',
    driver_email: order.block?.driver?.email ?? 'Inexistente',
    receiver_name: order.receptions?.[0]?.user?.name ?? 'Inexistente',
    bags_count: order.products?.length ?? 0,
    block_id: blockId,
    orders_count: ordersCount,
    incidences: order.incidences?.length ? order.incidences.map(i => i.description).join(', ') : 'Inexistente',
    incidence_status: order.incidences?.length
      ? order.incidences.map(i => getIncidenceStatusText(i.status)).join(', ')
      : 'Inexistente',
    receptions: order.receptions?.length
      ? order.receptions.map(r => ({
        id: r.id,
        reception_date: formatDate(r.reception_date),
        user_name: r.user?.name ?? 'Inexistente',
        user_email: r.user?.email ?? 'Inexistente',
      }))
      : []
  };
}

export function formatDate(dateStr: string): string {
  if (!dateStr) return '';
  const d = new Date(dateStr);
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${d.getFullYear()}-${month}-${day}`;
}
