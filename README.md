# 🚗 Vehicle Insurance ML Pipeline – Production-Ready MLOps Project

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue.svg">
  <img src="https://img.shields.io/badge/Framework-FastAPI-green.svg">
  <img src="https://img.shields.io/badge/Cloud-AWS-orange.svg">
  <img src="https://img.shields.io/badge/MLOps-CI%2FCD%2C%20Docker%2C%20MongoDB-success">
</p>

> **A full-stack, production-grade Machine Learning pipeline for Vehicle Insurance data – built with Clean Code, Cloud Services, Docker, CI/CD and AWS S3 integration.**

---

## 🌟 Highlights

✅ Professional project structure using Python packaging best practices

✅ End-to-end pipeline: Data ingestion → Validation → Transformation → Training → Evaluation → Deployment

✅ MongoDB Atlas used as a scalable NoSQL data storage

✅ AWS S3 integration for model registry

✅ Containerized using Docker, deployed via GitHub Actions to AWS EC2

✅ CI/CD pipeline for seamless automation and delivery

✅ User-friendly prediction interface with FastAPI

✅ Self-hosted GitHub Runner on EC2 instance for scalable builds

---

## 🚀 Project Setup

### 🧱 1. Template & Virtual Environment

```bash
# Create file structure
python template.py

# Setup environment
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
pip list  # Verify installations
```

> 📌 **Local imports** handled via `setup.py` and `pyproject.toml`. Learn more inside [`crashcourse.txt`](./crashcourse.txt).

---

## 🌐 MongoDB Atlas Setup

1. Signup at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create new project → create M0 cluster → setup DB user & password
3. Add IP `0.0.0.0/0` in **Network Access**
4. Copy Python connection string and securely store it (replace `<password>`)
5. Create `notebook/mongoDB_demo.ipynb` → use `vehicle` kernel
6. Load dataset & push to MongoDB using PyMongo
7. Confirm upload from Atlas Dashboard → Collections view

---

## ⚙️ Logging, Exceptions & Notebooks

* ✍️ Modular logging system: `logger.py`
* ❌ Custom exceptions for debugging: `exception.py`
* 📊 Exploratory Data Analysis and Feature Engineering notebooks provided

---

## 📥 Data Ingestion Pipeline

* Define schema in `constants/__init__.py`
* Setup MongoDB connection in `configuration/mongo_db_connection.py`
* Fetch and convert data to DataFrame via `data_access/proj1_data.py`
* Create `DataIngestionConfig` and `DataIngestionArtifact` classes
* Pipeline logic in `components/data_ingestion.py`
* Trigger via `demo.py` with Mongo URL configured as:

### 🔐 Set Mongo URL in ENV

**Mac/Linux (Bash):**

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>..."
```

**Windows (PowerShell):**

```powershell
$env:MONGODB_URL="mongodb+srv://<username>:<password>..."
```

✅ Add `artifact/` to `.gitignore`

---

## 🧪 Data Validation, Transformation & Model Training

* Define schema in `config/schema.yaml`
* Core logic in `utils/main_utils.py`
* Implement Data Validation, Transformation, and Training as modular components
* Add `estimator.py` to support transformations & modeling

---

## ☁️ AWS Setup for Model Evaluation & Registry

### 🔑 IAM & S3 Setup

1. Login to AWS → Region: `us-east-1`
2. IAM → Create user `firstproj` with `AdministratorAccess`
3. Download Access Keys CSV
4. Export keys as ENV vars:

```bash
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
```

5. Create S3 bucket:

   * Name: `my-model-mlopsproj`
   * Uncheck “Block all public access”

6. Define in `constants/__init__.py`:

```python
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
MODEL_BUCKET_NAME = "my-model-mlopsproj"
MODEL_PUSHER_S3_KEY = "model-registry"
```

7. Add logic to `src/aws_storage/` and `entity/s3_estimator.py`

---

## 📊 Model Evaluation & Pushing

* Evaluate model drift
* Push model artifacts to S3
* Deploy latest version with version tracking

---

## 🧠 Prediction Pipeline

* Add `app.py` to serve FastAPI-based inference
* Add UI resources to `static/` and `templates/`

---

## ⚙️ CI/CD + Docker + GitHub Actions

### 🐳 Docker Setup

* Create `Dockerfile` and `.dockerignore`
* Add GitHub Workflow YAML: `.github/workflows/aws.yaml`

### 🔐 GitHub Secrets

Add the following secrets in GitHub → Settings → Actions:

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `AWS_DEFAULT_REGION`
* `ECR_REPO`

### 🏗️ Self-Hosted Runner (EC2)

1. Launch EC2 Ubuntu instance (T2 Medium)
2. SSH into EC2 → install Docker:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

3. Connect GitHub Runner:

   * Settings → Actions → New self-hosted runner
   * Follow Linux commands from GitHub on EC2

4. Run `./run.sh` to activate runner

---

## 🌍 Deploy to EC2

1. Create Inbound Rule in EC2:

   * Port: `5080` → IP: `0.0.0.0/0`
2. Visit `http://<EC2_PUBLIC_IP>:5080` to launch the app
3. Access `/training` route to retrain model

---

## 📁 Directory Structure

```
📦Vehicle-ML-Pipeline
 ┣ 📂src
 ┃ ┣ 📂components
 ┃ ┣ 📂data_access
 ┃ ┣ 📂entity
 ┃ ┣ 📂configuration
 ┃ ┣ 📂aws_storage
 ┃ ┣ 📂utils
 ┣ 📂templates
 ┣ 📂static
 ┣ 📂notebook
 ┣ 📜Dockerfile
 ┣ 📜app.py
 ┣ 📜setup.py
 ┣ 📜pyproject.toml
 ┣ 📜requirements.txt
 ┣ 📜README.md
 ┗ 📂.github/workflows
```

---

## 👨‍💻 Author

**Harshwardhan Ghongade**
🚀 Passionate about ML, Deep Learning & MLOps
🎓 Undergraduate at IIT Kanpur



