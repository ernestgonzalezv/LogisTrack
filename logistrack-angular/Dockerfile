# -----------------------
# Etapa 1: Build Angular
# -----------------------
FROM node:20-alpine AS build

WORKDIR /app

# Copiar solo package.json y package-lock.json para cache de dependencias
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto del proyecto Angular
COPY . .

# Build de producción
RUN npm run build -- --output-path=dist/logistrack-angular --configuration=production

# -----------------------
# Etapa 2: Servir con Nginx
# -----------------------
FROM nginx:alpine

# Limpiar html por defecto
RUN rm -rf /usr/share/nginx/html/*

# Copiar build de Angular al path que Nginx sirve
COPY --from=build /app/dist/logistrack-angular /usr/share/nginx/html

# Copiar configuración personalizada de Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exponer puerto 80
EXPOSE 80

# Iniciar Nginx en primer plano
CMD ["nginx", "-g", "daemon off;"]
