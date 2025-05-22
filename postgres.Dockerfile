# Dockerfile for PostgreSQL Database
#
# Builds a PostgreSQL 16 container for DevSecOps practice.
#
# Usage:
#   docker build -f postgres.Dockerfile -t devsecops-db .

# Use the official PostgreSQL image from Docker Hub
FROM postgres:16

# Set environment variables for default user and database
ENV POSTGRES_USER=appuser
ENV POSTGRES_PASSWORD=apppassword
ENV POSTGRES_DB=appdb

# Expose PostgreSQL port
EXPOSE 5432
