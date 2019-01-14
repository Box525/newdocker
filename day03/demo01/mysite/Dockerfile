FROM daocloud.io/python:3-onbuild
MAINTAINER box 12345@163.com

ADD . /mysite/
WORKDIR /mysite

RUN pip install -r requirements.txt
CMD ["python","app.py"]

