export enum OrderStatus {
  PREPARATION = 1,
  DISPATCHED = 2,
  EXPEDITION = 3,
  RECEIVED = 4,
  CONSOLIDATED = 5,
  DELIVERED = 6
}


export function getStatusText(status: number): string {
  switch (status) {
    case OrderStatus.PREPARATION:
      return 'Preparación';
    case OrderStatus.DISPATCHED:
      return 'Despachado';
    case OrderStatus.EXPEDITION:
      return "Expedición"
    case OrderStatus.RECEIVED:
      return 'Recibido';
    case OrderStatus.CONSOLIDATED:
      return 'Consolidado';
    case OrderStatus.DELIVERED:
      return 'Entregado';
    default:
      return 'Desconocido';
  }
}
