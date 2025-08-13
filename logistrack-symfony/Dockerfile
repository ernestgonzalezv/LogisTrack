FROM php:8.2-apache

RUN apt-get update && apt-get install -y \
    libicu-dev \
    libzip-dev \
    unzip \
    git \
    && docker-php-ext-install intl pdo pdo_mysql zip opcache

RUN pecl install redis && docker-php-ext-enable redis

COPY . /var/www/symfony

RUN chown -R www-data:www-data /var/www/symfony

RUN a2enmod rewrite

WORKDIR /var/www/symfony

EXPOSE 80

CMD ["apache2-foreground"]
