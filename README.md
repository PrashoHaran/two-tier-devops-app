# 🚀 Two-Tier Web Application – CI/CD with Docker & Jenkins

A two-tier web application with a fully automated CI/CD pipeline using Docker, Docker Compose, and Jenkins.
The pipeline builds, tests, and deploys the application automatically after every GitHub push.

---

## 📌 Project Overview

This project demonstrates a real-world DevOps workflow where:

- A Flask web application (frontend tier) connects to a MySQL database (backend tier)
- The application is fully containerized using Docker
- Jenkins automates:
  Code checkout
  Build
  Automated testing
  Deployment using Docker Compose
- Deployment happens only if tests pass

---

## 🏗️ Architecture

```
GitHub
   ↓
Jenkins CI/CD Pipeline
   ↓
Docker Build & Test
   ↓
Docker Compose Deployment
   ↓
Flask App  ←→  MySQL Database

```
---

## 🗂️ Project Structure

```
two-tier-devops-app/
│
├── app/
│   ├── app.py
│   └── templates/
│
├── tests/
│   └── test_app.py
│
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── requirements.txt
└── README.md

```
---

## 🧰 Tech Stack

🔹 Application
- Python
- Flask – lightweight web framework
- MySQL – relational database

🔹 DevOps & CI/CD
- Docker
- Docker Compose
- Jenkins
- Git & GitHub
- Pytest - automated testing

  🔹 Environment
- Linux (Ubuntu)
- Local development & CI environment
  
---

## 🔁 CI/CD Pipeline Stages

### 1. Checkout
- Jenkins pulls the latest code from GitHub

### 2. Build
- Docker image for the Flask app is built

### 3. Test
- A Python virtual environment is created
- Dependencies are installed
- Automated tests are executed using pytest

### 4. Deploy
- Existing containers are stopped safely
- Application is deployed using Docker Compose
- App runs on port 5000

---

## 🧪 Test-Gated Deployment (Key Feature)
If any test fails:
- **❌ Pipeline stops** 
- **🚫 Deployment is skipped**
- This ensures only tested code reaches deployment, following DevOps best practices.
---

## Screenshots

<img width="1837" height="847" alt="image" src="https://github.com/user-attachments/assets/337d659b-2110-43bb-acbe-1bdb21c024aa" />
<img width="1835" height="828" alt="Jenkins SS" src="https://github.com/user-attachments/assets/f9fd0d28-366b-40df-b634-a9d756ce255a" />

---

## 🚀 Future Enhancements

- Deploy Jenkins and app on AWS EC2
- Add GitHub Webhooks for auto-triggered builds
- Migrate to Kubernetes
- Add monitoring (Prometheus / Grafana)

---

**Stay Safe & Stay Informed.** 🦠📊✨
 
---
