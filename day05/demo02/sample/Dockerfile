FROM hub.c.163.com/library/httpd:latest
MAINTAINER box 12345@163.com

RUN mkdir -p /usr/local/apache2/htdocs/img
WORKDIR /usr/local/apache2

EXPOSE 80
ENTRYPOINT ["httpd"]
CMD ["-D","FOREGROUND"]