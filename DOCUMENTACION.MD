
---

# DOCUMENTACION.md – Prueba Técnica LogisTrack


## 1. Cómo resolví la prueba

La prueba se resolvió implementando la arquitectura híbrida propuesta: Symfony, Django y Angular, comunicándose mediante Redis y persisitiendo datos en MySQL.

**Flujo completo de bloques:**

1. **Symfony (PHP)** publica eventos de bloques logísticos en **Redis Streams** (`logistrack.blocks`) usando comandos de consola:

   ```bash
   docker compose exec symfony_app php bin/console logistrack:seed-blocks 5
   docker compose exec symfony_app php bin/console logistrack:publish-block
   ```

   Cada bloque contiene:

    * `id_orden`
    * `id_bloque`
    * `id_chofer`
    * `productos`
    * `fecha_despacho`

2. **Django (Python)** consume los bloques desde Redis, los persiste en **MySQL** y expone endpoints **REST**:

   ```bash
   docker compose exec django_app python manage.py create_db
   docker compose exec django_app python manage.py migrate
   docker compose exec django_app python manage.py sync_blocks
   ```

    * Arquitectura **Clean + CQRS**: Controllers → Mediator → Handlers → Repositories → DTOs → JSON
    * Paginación y filtros implementados según parámetros enviados desde Angular
    * **Unit tests con `pytest`**: Se escribieron pruebas unitarias para validar la lógica de negocio, transformaciones de DTOs, consultas a repositorios y handlers. Esto permitió detectar errores antes de la integración completa.
      Ejemplo de ejecución:

      ```bash
      docker compose exec django_app pytest -v
      ```

3. **Angular (Frontend)** consume la API REST de Django y muestra el ciclo logístico completo:

    * Componentes por proceso: `Despacho`, `Preparacion`, `Expedicion`, `Recepcion`, `Consolidacion`, `Distribucion`
    * Tablas dinámicas (`BaseTableComponent`) con paginación, filtros y mapeos de datos
    * Integración con **ApiService** para consultas y mappers para transformar DTOs a modelos Angular

4. **Docker Compose** orquesta todos los servicios:

    * Symfony: puerto 8000
    * Django: puerto 8080
    * Angular: puerto 4200
    * Redis: 6379
    * MySQL: 3306
    * phpMyAdmin: 8081

El flujo completo de la prueba:

```
PYMEs → Symfony → Redis → Django → MySQL → Angular → Usuario final
```

---

## 2. Decisiones técnicas y arquitectura general

* **Microservicios**: Separación de responsabilidades Symfony → Django → Angular
* **Redis Streams**: Bus de eventos asíncrono para bloques logísticos
* **Clean Architecture + CQRS**: En Django para mantener lógica de negocio separada de infraestructura
* **DTOs y Validaciones**: Garantizan integridad de datos entre servicios
* **Docker Compose**: Reproducibilidad y aislamiento de servicios
* **Angular Material + TailwindCSS**: UI consistente y responsive
* **Comandos de prueba**: Symfony y Django permiten generar datos de prueba y sincronizar bloques

**Arquitectura resumida:**

```
Symfony → Redis → Django → MySQL → Angular
```

---

## 3. Herramientas de IA utilizadas

* **GitHub Copilot**:

    * Sugerencias de código, funciones, mapeos y organización de carpetas en Angular y Django
    * Ejemplos de DTOs, mappers y serializers
* **ChatGPT**:

    * Ideas rápidas de documentación y revisión de arquitectura
    * Claridad en flujo de eventos y comunicación entre servicios

**Beneficios de la IA:**

* Ahorro de tiempo evitando escribir código repetitivo
* Ejemplos claros de validaciones y transformaciones
* Mejora de documentación y estructura de proyecto

---

## 4. Retos encontrados y cómo los resolví

| Reto                                             | Solución                                                                                                 |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Sincronización de bloques entre Symfony y Django | Implementé Redis Streams (`logistrack.blocks`) y comando `sync_blocks` en Django                         |
| Consistencia de datos                            | Usé DTOs, validaciones y mapeos Domain → DTO → JSON                                                      |
| Modularidad y mantenibilidad                     | Separé capas en Symfony, Django y Angular, usando Clean Architecture y componentes Angular reutilizables |
| UI profesional y responsive                      | Uso de Angular Material + TailwindCSS, tablas dinámicas y menús laterales                                |
| Datos de prueba y verificación                   | Comandos Symfony y Django permiten sembrar bloques y verificar flujo completo                            |

---

