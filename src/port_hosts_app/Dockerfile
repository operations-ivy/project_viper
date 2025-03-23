FROM python:3.9-alpine
RUN apk add --no-cache openrc curl nmap
RUN rc-update add sshd
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN mkdir -p /app/templates
COPY templates/index.html templates/index.html
COPY port_hosts.py port_hosts.py
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
            CMD curl -f http://localhost:5000/health || exit 1
ENTRYPOINT [ "python3", "port_hosts.py" ]
