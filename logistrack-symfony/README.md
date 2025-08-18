# Prueba Técnica LogisTrack – Microservicio Symfony

[![codecov](https://codecov.io/github/ernestgonzalezv/LogisTrack/graph/badge.svg?token=8R68FOULQG)](https://codecov.io/github/ernestgonzalezv/LogisTrack)

## Descripción del Microservicio

El microservicio Symfony forma parte del backend monolítico que publica eventos de bloques consolidados listos para distribución. Los datos generados se sincronizan con otros microservicios modernos (Django REST Framework) usando Redis como bus de eventos.

---

## Objetivo del Microservicio Symfony

El microservicio se encarga de:

1. Publicar eventos de bloques listos para distribución a Redis.
2. Permitir la inserción de datos de prueba mediante comandos de consola.
3. Garantizar la integridad de los datos mediante validaciones y DTOs.

Cada evento publicado contiene:

* `id_orden`
* `id_bloque`
* `id_chofer`
* `productos`
* `fecha_despacho`

---

## Arquitectura

Se sigue el patrón **Clean Architecture**, con separación de responsabilidades clara:

* **Domain:** Modelos (`Block`), excepciones y repositorios (`BlockPublisherInterface`).
* **Application:** Casos de uso (`PublishBlockUseCase`), DTOs, mappers y validadores.
* **Infrastructure:** Implementación concreta del repositorio en Redis (`RedisBlockPublisher`, `RedisClient`).
* **Presentation:** Comandos Symfony (`PublishBlockCommand`, `SeedBlocksCommand`) y controladores API.
* **i18n:** Mensajes de validación traducibles mediante Symfony Translator.

El microservicio se integra con otros sistemas mediante Redis Streams (`logistrack.blocks`) para un flujo de datos asíncrono y escalable.

---

## Estructura del Proyecto (src/)

```
src/
├── Kernel.php
├── Application/
│   ├── Constants/ApiEndpoints.php
│   ├── DTO/Block/
│   │   ├── BlockDTO.php
│   │   ├── request/BlockPublishRequest.php
│   │   └── response/BlockPublishResponse.php
│   ├── Mappers/Block/
│   │   ├── BlockMapper.php
│   │   └── BlockPublishRequestToDtoMapper.php
│   ├── UseCases/Block/PublishBlockUseCase.php
│   └── Validators/Block/BlockPublishRequestValidator.php
├── Domain/
│   ├── Exception/BlockPublishingException.php
│   ├── Model/Block.php
│   └── Repository/BlockPublisherInterface.php
├── Infrastructure/Redis/
│   ├── RedisBlockPublisher.php
│   └── RedisClient.php
└── Presentation/
    ├── Console/PublishBlockCommand.php
    ├── Console/SeedBlocksCommand.php
    └── Controller/BlockController.php
```

---

## Requisitos Técnicos Cumplidos

1. **Symfony (PHP)**

    * Publicación de eventos de bloques en Redis usando Redis Streams.
    * Comandos de consola para insertar bloques de prueba (`logistrack:seed-blocks`).
    * Validaciones estrictas con Symfony Validator.
    * Traducción de mensajes con Symfony Translator (i18n).

2. **Persistencia y Event Bus**

    * Redis Streams (`logistrack.blocks`) para manejo de eventos.
    * Transformación de objetos Domain a DTOs y a Redis (JSON strings).

3. **Dockerizado**

    * `Dockerfile` con PHP 8.2 y Apache, extensiones instaladas (`pdo_mysql`, `intl`, `zip`, `redis`).
    * `docker-compose.yml` con servicios `symfony_app` y `redis_server`.
    * Volúmenes persistentes para Redis (`redis-data`).

---

## Instalación y Ejecución

### Prerrequisitos

* Docker
* Docker Compose

### Levantar el proyecto

```bash
docker-compose up --build -d
```

### Verificar contenedores

```bash
docker-compose ps
```

### Comandos Symfony dentro del contenedor

* Sembrar bloques de prueba:

```bash
docker-compose exec symfony_app php bin/console logistrack:seed-blocks 10
```

* Publicar un bloque manual:

```bash
docker-compose exec symfony_app php bin/console logistrack:publish-block
```

### Verificar datos en Redis

```bash
docker exec -it redis_server redis-cli
XRANGE logistrack.blocks - +
```

---

## Dependencias Clave

* `symfony/framework-bundle`
* `symfony/console`
* `symfony/validator`
* `symfony/translation`
* `predis/predis`
* PHP Extensions: `pdo_mysql`, `intl`, `zip`, `redis`, `opcache`

---

## Consideraciones Técnicas

* Eventos de bloques se publican de manera asíncrona en Redis Streams.
* DTOs garantizan consistencia y tipado de los datos.
* Validaciones y traducciones permiten internacionalización y robustez.
* Arquitectura modular (Clean Architecture) facilita mantenimiento y pruebas.
* Docker y Docker Compose permiten reproducibilidad del entorno local y de despliegue.

---

## Comandos Útiles

| Comando                                           | Descripción                                     |
| ------------------------------------------------- | ----------------------------------------------- |
| `docker-compose up --build -d`                    | Construye y levanta contenedores.               |
| `docker-compose exec symfony_app php bin/console` | Ejecuta comandos Symfony dentro del contenedor. |
| `logistrack:seed-blocks [count]`                  | Sembrar bloques aleatorios para prueba.         |
| `logistrack:publish-block`                        | Publicar un bloque manualmente.                 |
| `docker exec -it redis_server redis-cli`          | Acceder a Redis CLI para inspección.            |

---

## Próximos pasos / Integración

* Django REST Framework consumirá los eventos de Redis y persistirá en su base de datos.
* Angular consumirá la API de Django para mostrar los bloques, choferes y estados de confirmación.
