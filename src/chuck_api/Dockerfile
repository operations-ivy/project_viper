FROM python:3.9-alpine
RUN apk add --no-cache curl
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN mkdir -p /app/templates
COPY templates/index.html templates/index.html
COPY ssh_hosts.py ssh_hosts.py
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
            CMD curl -f http://localhost:5000/health || exit 1
ENTRYPOINT [ "python3", "ssh_hosts.py" ]