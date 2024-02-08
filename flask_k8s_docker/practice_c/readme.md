https://medium.com/featurepreneur/deploying-a-flask-app-to-kubernetes-f05c93866aff

create flask app app.py
create dockerfile
push app.py and dockerfile to github
start minikube and ssh into minikube
clone git repo
build and tag docker image
push docker image to docker hub
create deployment and service yaml
apply service and deployment to minikube with kubectl
kubectl service to get service in browser