FROM python:3.9-alpine
RUN apk add git
WORKDIR /app
RUN git clone https://github.com/operations-ivy/project_viper.git
RUN cd project_viper/flask_k8s_docker
RUN pip install -r /app/project_viper/flask_k8s_docker/requirements.txt
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
            CMD curl -f http://localhost:5000/health || exit 1
ENTRYPOINT [ "python", "/app/project_viper/flask_k8s_docker/src/app.py" ]