FROM python:3.9-alpine
RUN apk add --no-cache curl
WORKDIR /app
RUN touch /app/sqlite.db
ENV DB_LOCATION=/app/sqlite.db
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# RUN mkdir -p /app/templates
# COPY templates/index.html templates/index.html
COPY joke_importer.py joke_importer.py
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
            CMD curl -f http://localhost:5000/health || exit 1
ENTRYPOINT [ "python3", "joke_importer.py" ]