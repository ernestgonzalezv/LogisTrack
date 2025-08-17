FROM php:8.2-apache

# Instalar dependencias de sistema y extensiones PHP
RUN apt-get update && apt-get install -y \
    libicu-dev \
    libzip-dev \
    unzip \
    git \
    curl \
    && docker-php-ext-install intl pdo pdo_mysql zip opcache \
    && pecl install redis \
    && docker-php-ext-enable redis \
    && a2enmod rewrite

WORKDIR /var/www/symfony

# Copiar TODO el proyecto antes de composer install
COPY . .

# Instalar Composer globalmente
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Instalar dependencias PHP (producción)
RUN composer install --no-dev --optimize-autoloader --prefer-dist --no-interaction --ignore-platform-reqs

# Ajustar permisos
RUN chown -R www-data:www-data /var/www/symfony

EXPOSE 80

CMD ["apache2-foreground"]
