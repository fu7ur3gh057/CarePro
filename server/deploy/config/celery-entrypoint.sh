#!/bin/sh

# CELERY WORKER & BEAT
until cd /app/server; do
  echo "Waiting for server volume..."
done

# run a worker and beat
celery -A server worker --beat --scheduler django --loglevel=info