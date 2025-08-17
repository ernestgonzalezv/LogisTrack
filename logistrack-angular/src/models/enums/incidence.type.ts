export enum IncidenceType {
  DAMAGED = 1,     // Dañada
  MISSING = 2,     // Faltante
  LATE = 3,        // Tarde
  WRONG_ITEM = 4   // Artículo incorrecto
}

export function getIncidenceTypeText(type: IncidenceType): string {
  switch (type) {
    case IncidenceType.DAMAGED:
      return `Dañada`;
    case IncidenceType.MISSING:
      return `Faltante`;
    case IncidenceType.LATE:
      return `Tarde`;
    case IncidenceType.WRONG_ITEM:
      return `Artículo incorrecto`;
    default:
      return `Desconocido`;
  }
}
