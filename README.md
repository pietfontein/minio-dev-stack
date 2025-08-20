A complete Docker-based MinIO object storage setup for local development and testing.

## 🚀 Features

- **MinIO Server** - S3-compatible object storage
- **Web Console** - Access at http://localhost:9001
- **MC Client** - Built-in management client
- **Pre-configured** - Ready for Python, AWS CLI, and SDKs
- **Versioning Support** - Object versioning enabled

## 📦 Quick Start

```bash
# Start the stack
docker-compose up -d

# Access the web console:
# URL: http://localhost:9001
# User: admin
# Pass: password123

# Use the MC client
docker-compose exec mc mc ls local/

# Or use AWS CLI
aws --endpoint-url http://localhost:9000 s3 ls
