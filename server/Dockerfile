FROM python:3.11-slim

ENV PYTHONBUFFERED=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

ENV APP=/app

# The dealership database service and the sentiment analyzer service.  On a
# developer machine they run on the host, so `host.docker.internal` is used.
ENV backend_url=http://host.docker.internal:3030
ENV sentiment_analyzer_url=http://host.docker.internal:5050/

# Change the workdir.
WORKDIR $APP

# Install the requirements
COPY requirements.txt $APP

RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the files
COPY . $APP

EXPOSE 8000

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangobackend.wsgi"]
