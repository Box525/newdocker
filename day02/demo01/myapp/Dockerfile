# TODO:指定一个构建镜像的基础源镜像，必写
FROM daocloud.io/python:3-onbuild
# TODO:描述镜像的创建者，名称和邮箱
MAINTAINER box 1234@163.com
# TODO: . 将宿主机当前目录所有的文件 copy到容器中/www/目录下
COPY . /www/
# TODO: RUN 创建镜像的命令 执行之后就会生产一个新的镜像
RUN pip install -r requirements.txt
EXPOSE 8888 9999
# TODO: 指定工作目录
WORKDIR /www
CMD ["python","app.py"]





