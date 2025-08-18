from typing import Optional, List, Union
from datetime import datetime

class RedisBlock:
    """
    Modelo de dominio que representa un bloque tal como se obtiene de Redis.
    """
    def __init__(
        self,
        id_bloque: str,
        id_orden: str,
        id_chofer: Optional[str] = None,
        fecha_despacho: Optional[Union[str, datetime]] = None,
        productos: Optional[Union[str, List[dict]]] = None
    ):
        self.id_bloque = id_bloque
        self.id_orden = id_orden
        self.id_chofer = id_chofer
        self.fecha_despacho = fecha_despacho
        # Puede venir como JSON string o lista de dicts
        self.productos = productos or []
