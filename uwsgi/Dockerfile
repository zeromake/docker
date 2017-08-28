FROM zeromake/base-uwsgi:0.1

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt -i https://mirrors.ustc.edu.cn/pypi/web/simple

RUN rm -rf /tmp/requirements.txt

WORKDIR /data/web/

CMD ["uwsgi", "--ini", "/data/web/uwsgi.ini"]
