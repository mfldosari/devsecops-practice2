# DevSecOps Practice Project

This project is a hands-on DevSecOps lab featuring a vulnerable Python Flask web application and a PostgreSQL database, both containerized for local development and security testing. It is designed to help you practice secure coding, static and dynamic security scanning, and container security in a realistic workflow.

## Features
- **Vulnerable Flask App**: A simple web interface that allows raw SQL queries (intentionally SQL injectable for learning purposes).
- **PostgreSQL Database**: Runs in a separate container, pre-configured for the app.
- **Dockerized**: Both app and database run via Docker Compose for easy setup.
- **Security Headers**: The app sets modern HTTP security headers for best practices.
- **DevSecOps Workflows**:
  - **SAST**: Bandit static analysis and Trivy container scanning run on every push/PR via GitHub Actions.
  - **DAST**: OWASP ZAP dynamic scan workflow, manually triggerable from GitHub Actions.
- **Remediation**: The project demonstrates how to fix vulnerabilities flagged by Bandit, Trivy, and ZAP.

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.11+](https://www.python.org/downloads/)

### Local Development
1. **Clone the repository:**
   ```bash
   git clone https://github.com/mfldosari/devsecops-practice2.git
   cd devsecops-practice2
   ```
2. **Build and start the containers:**
   ```bash
   docker compose up --build
   ```
3. **Access the app:**
   - Open [http://localhost:5000](http://localhost:5000) in your browser.
   - Use the web form to run SQL queries (for educational purposes only).

### Security Scanning

#### Static & Container Scanning (SAST)
- On every push/PR, GitHub Actions runs:
  - **Bandit**: Scans Python code for security issues.
  - **Trivy**: Scans the app Docker image for OS and Python package vulnerabilities.
- Reports are uploaded as workflow artifacts.

#### Dynamic Scanning (DAST)
- Manually trigger the `DAST` workflow in GitHub Actions to run an OWASP ZAP scan against the running app.
- The ZAP HTML report is uploaded as an artifact.

## Security Remediation
- The app and its dependencies are regularly updated to address vulnerabilities flagged by Bandit, Trivy, and ZAP.
- Security headers and best practices are implemented in the Flask app.

## Educational Purpose
**Warning:** This app is intentionally vulnerable to SQL injection and is for educational/testing use only. **Do not deploy in production.**

## Project Structure
```
app.py                # Flask web app (intentionally vulnerable)
docker-compose.yml    # Orchestrates app and database containers
Dockerfile            # Builds the Flask app container
postgres.Dockerfile   # Builds the PostgreSQL container
requirements.txt      # Python dependencies
.github/workflows/    # CI/CD and security scan workflows
```

## License
MIT