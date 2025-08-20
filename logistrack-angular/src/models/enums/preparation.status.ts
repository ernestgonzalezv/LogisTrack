// preparation-status.enum.ts
export enum PreparationStatus {
  PENDING = 0,   // Pendiente
  COMPLETE = 1   // Completo
}

export function getPreparationStatusText(status: PreparationStatus): string {
  switch (status) {
    case PreparationStatus.PENDING:
      return `Pendiente`;
    case PreparationStatus.COMPLETE:
      return `Completo`;
    default:
      return `Desconocido`;
  }
}
