# LogisTrack Symfony Microservice

## Overview

This Symfony microservice publishes "blocks" of logistics orders to Redis streams, following a Clean Architecture pattern with Mapper classes for DTO <-> Domain transformations.

## Setup

### Requirements

- Docker and Docker Compose installed
- PHP 8.2+
- Composer

### Running with Docker

```bash
docker-compose up -d
docker exec -it logistrack_php bash

# Inside container:
composer install
php bin/console logistrack:seed-blocks 5
