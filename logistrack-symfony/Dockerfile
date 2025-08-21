FROM php:8.2-apache

# Instalar dependencias de sistema y extensiones PHP
RUN apt-get update && apt-get install -y \
    libicu-dev \
    libzip-dev \
    unzip \
    git \
    curl \
    && docker-php-ext-install intl pdo pdo_mysql zip opcache \
    && pecl install redis xdebug \
    && docker-php-ext-enable redis xdebug \
    && a2enmod rewrite

WORKDIR /var/www/symfony

# Copiar TODO el proyecto antes de composer install
COPY . .

# Copiar archivo de configuración de PHPUnit
COPY phpunit.xml.dist /var/www/symfony/phpunit.xml.dist

# Instalar Composer globalmente
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Instalar PHPUnit globalmente
RUN curl -L https://phar.phpunit.de/phpunit-10.phar -o /usr/local/bin/phpunit \
    && chmod +x /usr/local/bin/phpunit

# Instalar dependencias PHP (producción + dev para tests)
RUN composer install --optimize-autoloader --prefer-dist --no-interaction --ignore-platform-reqs

# Instalar dependencias dev necesarias para WebTestCase
RUN composer require --dev symfony/browser-kit symfony/http-client --ignore-platform-reqs

# Configurar Xdebug para coverage
RUN echo "xdebug.mode=coverage" > /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.start_with_request=no" >> /usr/local/etc/php/conf.d/xdebug.ini

# Ajustar permisos
RUN chown -R www-data:www-data /var/www/symfony

EXPOSE 80

CMD ["apache2-foreground"]
