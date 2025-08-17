export enum IncidenceStatus {
  OPEN = 1,        // Abierta
  IN_PROGRESS = 2, // En progreso
  RESOLVED = 3,    // Resuelta
  CLOSED = 4       // Cerrada
}

export function getIncidenceStatusText(status: IncidenceStatus): string {
  switch (status) {
    case IncidenceStatus.OPEN:
      return `Abierta`;
    case IncidenceStatus.IN_PROGRESS:
      return `En progreso`;
    case IncidenceStatus.RESOLVED:
      return `Resuelta`;
    case IncidenceStatus.CLOSED:
      return `Cerrada`;
    default:
      return `Desconocido`;
  }
}
