# Clarity Reports - Deployment Guide

## 1. Prerequisites
Ensure the following are installed before deployment:
- **Python 3.9+**
- **PostgreSQL 14+**
- **Docker & Docker Compose** (for containerized deployment)
- **Nginx** (for reverse proxy)
- **Git** (for version control)

---

## 2. Setting Up the Server
### **Install Dependencies**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv postgresql postgresql-contrib nginx
```

### **Create a Deployment Directory**
```bash
mkdir -p /opt/clarity_reports && cd /opt/clarity_reports
git clone https://github.com/your_repo/clarity_reports.git .
```

---

## 3. Configure PostgreSQL
```bash
sudo -u postgres psql
CREATE DATABASE clarity_reports;
CREATE USER clarity_user WITH ENCRYPTED PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE clarity_reports TO clarity_user;
```

---

## 4. Set Up Environment Variables
Create a `.env` file in the project root (ensure it is added to `.gitignore` to prevent accidental exposure):
```plaintext
DATABASE_URL=postgresql://clarity_user:your_password@localhost:5432/clarity_reports
SECRET_KEY=your_secret_key
NEWS_API_KEY=your_news_api_key
```

---

## 5. Running the Application
### **Option 1: Running with Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r docs/requirements.txt
uvicorn backend.api.main:app --host 0.0.0.0 --port 8000 --reload
```

### **Option 2: Running with Docker**
Ensure Docker is installed, then create `docker-compose.yml`:
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    env_file: .env
    depends_on:
      - db
  db:
    image: postgres:14
    restart: always
    environment:
      POSTGRES_USER: clarity_user
      POSTGRES_PASSWORD: your_password
      POSTGRES_DB: clarity_reports
    ports:
      - "5432:5432"
```

Deploy with:
```bash
docker-compose up -d --build
```

---

## 6. Configure Nginx Reverse Proxy (Optional)
Create an Nginx configuration file `/etc/nginx/sites-available/clarity_reports`:
```plaintext
server {
    listen 80;
    server_name your_domain.com;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Redirect HTTP to HTTPS
    if ($scheme != "https") {
        return 301 https://$host$request_uri;
    }
}
```
Enable the configuration:
```bash
sudo ln -s /etc/nginx/sites-available/clarity_reports /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

---

## 7. Testing the Deployment
Verify the API is running:
```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/docs
```

---

## 8. Scaling & Future Considerations
- Use **Gunicorn** for production instead of Uvicorn directly.
- Move to **AWS/GCP** for cloud-based scalability.
- Implement **Redis + Celery** for background task processing.

🚀 **Clarity Reports is now deployed!**
