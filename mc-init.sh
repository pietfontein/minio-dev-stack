#!/bin/sh
set -e

echo "Waiting for MinIO to be ready..."
while ! curl -f http://minio:9000/minio/health/live >/dev/null 2>&1; do
    sleep 2
done

echo "Setting up MC alias..."
mc alias set local http://minio:9000 minioadmin minioadmin

echo "MC initialization completed successfully"
