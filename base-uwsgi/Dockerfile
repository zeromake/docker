FROM alpine:3.6

MAINTAINER zeromake <a390720046@gmail.com>

# 更换到阿里云
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

# 设置时区语言
ENV TZ Asia/Shanghai
ENV PYTHONIOENCODING utf8

COPY requirements.txt /tmp/requirements.txt

RUN apk add --no-cache gcc g++ make python2 py2-pip python2-dev pcre-dev jpeg-dev

# 设置默认编码
RUN sed -i 's/encoding = "ascii"/encoding = "utf8"/g' /usr/lib/python2.7/site.py

# 设置默认pip镜像
RUN mkdir -p ~/.pip && echo -e "[global]\ntimeout = 6000\nindex-url = https://pypi.doubanio.com/simple\n\n[install]\nuse-mirrors = true\nmirrors = https://pypi.doubanio.com/simple\ntrusted-host = pypi.doubanio.com" > ~/.pip/pip.conf

# 安装python包的依赖
RUN apk add --no-cache --virtual .build-deps mariadb-dev linux-headers postgresql-dev && \
    pip install uwsgi --no-cache-dir && \
    pip install numpy --no-cache-dir && \
    pip install  -r /tmp/requirements.txt --no-cache-dir && \
    apk del .build-deps && \
    find /usr/local -depth \
		\(\
			\( -type d -a \( -name test -o -name tests \) \) \
			-o \
			\( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
		\) -exec rm -rf '{}' +
RUN apk add --no-cache mariadb-client-libs libpq tzdata

RUN rm -rf /tmp/requirements.txt

RUN sed -i 's/>= 80300/>= 80301/g' /usr/lib/python2.7/site-packages/psycopg2/extras.py
