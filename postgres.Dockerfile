# Use the official PostgreSQL image from Docker Hub
FROM postgres:16

# Set environment variables for default user and database
ENV POSTGRES_USER=appuser
ENV POSTGRES_PASSWORD=apppassword
ENV POSTGRES_DB=appdb

# Expose PostgreSQL port
EXPOSE 5432
