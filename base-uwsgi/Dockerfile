FROM alpine:3.6

MAINTAINER zeromake <a390720046@gmail.com>

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

#设置时区语言
ENV TZ Asia/Shanghai

COPY requirements.txt /tmp/requirements.txt

RUN apk add --no-cache gcc g++ make python2 py2-pip python2-dev

RUN apk add --no-cache --virtual .build-deps mariadb-dev linux-headers postgresql-dev pcre-dev jpeg-dev && \
    pip install uwsgi -i https://pypi.doubanio.com/simple && \
    pip install numpy -i https://pypi.doubanio.com/simple --no-cache-dir && \
    pip install  -r /tmp/requirements.txt -i https://pypi.doubanio.com/simple/ --no-cache-dir && \
    apk del .build-deps && \
    find /usr/local -depth \
		\(\
			\( -type d -a \( -name test -o -name tests \) \) \
			-o \
			\( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
		\) -exec rm -rf '{}' +

RUN rm -rf /tmp/requirements.txt

RUN sed -i 's/>= 80300/>= 80301/g' /usr/lib/python2.7/site-packages/psycopg2/extras.py