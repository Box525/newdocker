FROM hub.c.163.com/library/httpd:latest
MAINTAINER box 123456@163.com

RUN mkdir -p /usr/local/apache2/htdocs/sources/
RUN mkdir -p /usr/local/apache2/htdocs/sources/css/
RUN mkdir -p /usr/local/apache2/htdocs/sources/js/
RUN mkdir -p /usr/local/apache2/htdocs/sources/img/

WORKDIR /usr/local/apache2

ENTRYPOINT ["httpd"]
CMD ["-D","FOREGROUND"]
