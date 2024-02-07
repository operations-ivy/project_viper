https://thecodinginterface.com/blog/flask-rest-api-minikube/

create flask app app.py
creat Dockerfile
build docker image and tag
push docker image to docker hub
create flask app deployment
create flask app service

service is loadbalancer so it needs `minikube tunnel` to connect

view external endpoint from created k8s service