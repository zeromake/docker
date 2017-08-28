DOCKERNAME = test-uwsgi
DOCKERIMAGE = zeromake/uwsgi:0.1
PWD = $(shell pwd)

build:
	docker build -t $(DOCKERIMAGE) .
clean:
	docker rmi $(DOCKERIMAGE)
run:
	docker run --name $(DOCKERNAME) -d -v $(PWD):/data/web:rw -p 9033:9033 $(DOCKERIMAGE)
restart:
	docker restart $(DOCKERNAME)
stop:
	docker stop $(DOCKERNAME)
start:
	docker start $(DOCKERNAME)
del:
	docker rm $(DOCKERNAME)
