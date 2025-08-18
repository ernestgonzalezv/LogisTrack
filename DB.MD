
---

# LogisTrack Database
---

## Esquema de Base de Datos

![database_scheme](assets/db.png)

El microservicio utiliza MySQL. A continuación se muestra el **modelo relacional** de la base de datos:

### Tablas principales

**Pyme**

* `id` UUID \[PK]
* `name` varchar
* `city` varchar

**DistributionCenter**

* `id` UUID \[PK]
* `name` varchar
* `city` varchar

**Driver**

* `id` UUID \[PK]
* `name` varchar
* `phone` varchar
* `email` varchar

**Product**

* `id` UUID \[PK]
* `sku` varchar
* `name` varchar
* `description` text

**Order**

* `id` UUID \[PK]
* `pyme_id` UUID \[FK → Pyme.id]
* `distribution_center_id` UUID \[FK → DistributionCenter.id]
* `dispatch_date` datetime
* `status` int *(Enum OrderStatus)*
* `total_weight` float
* `total_volume` float

**Block**

* `id` UUID \[PK]
* `creation_date` datetime
* `driver_id` UUID \[FK → Driver.id]

**OrderProduct**

* `id` UUID \[PK]
* `order_id` UUID \[FK → Order.id]
* `product_id` UUID \[FK → Product.id]
* `quantity` int

**BlockOrder**

* `id` UUID \[PK]
* `block_id` UUID \[FK → Block.id]
* `order_id` UUID \[FK → Order.id]

**Incidencia**

* `id` UUID \[PK]
* `order_id` UUID \[FK → Order.id]
* `tipo` varchar
* `descripcion` text
* `fecha` datetime
* `estado` int *(Enum IncidenciaStatus)*

---

### Relaciones

* Un **Order** pertenece a una **Pyme** y a un **DistributionCenter**.
* Un **Order** puede tener muchos **Products** a través de **OrderProduct**.
* Un **Block** está asignado a un **Driver** y puede contener muchas órdenes (**BlockOrder**).
* Cada **Incidencia** está asociada a una **Order**.

> Este diseño permite trazar el flujo completo de cada orden desde despacho hasta distribución final, incluyendo agrupación de órdenes en bloques, asignación a choferes y registro de incidencias.

---
