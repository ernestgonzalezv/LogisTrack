// distribution-status.enum.ts
export enum DistributionStatus {
  PENDING = 0,    // Pendiente
  DELIVERED = 1,  // Entregado
  REJECTED = 2    // Rechazado
}

export function getDistributionStatusText(status: DistributionStatus): string {
  switch (status) {
    case DistributionStatus.PENDING:
      return `Pendiente`;
    case DistributionStatus.DELIVERED:
      return `Entregado`;
    case DistributionStatus.REJECTED:
      return `Rechazado`;
    default:
      return `Desconocido`;
  }
}
