FROM alpine:latest

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && apk add --no-cache mariadb-dev gcc g++ make python2 python2-dev py2-pip linux-headers

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt -i https://mirrors.ustc.edu.cn/pypi/web/simple

RUN mkdir -p /data/web/ && pip install uwsgi -i https://mirrors.ustc.edu.cn/pypi/web/simple
WORKDIR /data/web/

CMD ["uwsgi", "--ini", "/data/web/uwsgi.ini"]