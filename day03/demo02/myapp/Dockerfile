FROM hub.c.163.com/library/python:latest
MAINTAINER box 1234@163.com

ADD . /www/
WORKDIR /www

RUN pip install -r requirements.txt
CMD ["python","app.py"]