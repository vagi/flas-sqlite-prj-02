# This file will fetch an image of NGINX
# from docker-hub and change default config file
FROM nginx:1.21.0

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/default.conf /etc/nginx/conf.d/
