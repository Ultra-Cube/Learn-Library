# 🚀 DevOps Tools Reference

> **UltraCube Learn-Library** | DevOps & Automation Tools Guide  
> **Author**: UltraCube DevOps Engineering Team  
> **Version**: 1.0 | **Last Updated**: 2025-01-12

![DevOps Banner](https://via.placeholder.com/800x150/FF6B35/FFFFFF?text=UltraCube+%7C+DevOps+Tools)

---

## 🎯 **Overview**

Essential DevOps tools and automation platforms used throughout the UltraCube Learn-Library DevOps curriculum. This guide covers CI/CD pipelines, containerization, orchestration, monitoring, and infrastructure automation.

### 🛠️ **DevOps Tool Categories**

| Category | Tools | Difficulty | Primary Use |
|----------|-------|------------|-------------|
| **Version Control** | Git, GitHub Actions | ⭐⭐☆☆☆ | Code management & CI/CD |
| **Containerization** | Docker, Podman | ⭐⭐⭐☆☆ | Application packaging |
| **Orchestration** | Kubernetes, Docker Swarm | ⭐⭐⭐⭐☆ | Container management |
| **CI/CD** | Jenkins, GitLab CI | ⭐⭐⭐☆☆ | Automation pipelines |
| **Infrastructure** | Terraform, Ansible | ⭐⭐⭐⭐☆ | Infrastructure as Code |
| **Monitoring** | Prometheus, Grafana | ⭐⭐⭐☆☆ | System observability |

---

## 🚀 **Quick Start Path**

### **Learning Progression**
1. **Git & GitHub** (version control fundamentals)
2. **Docker** (containerization basics)
3. **Jenkins or GitHub Actions** (CI/CD introduction)
4. **Kubernetes** (orchestration)
5. **Terraform** (infrastructure automation)
6. **Monitoring stack** (observability)

---

## 📂 **Version Control & CI/CD**

### **1. Git**

#### **📖 Overview**
Distributed version control system essential for modern DevOps workflows.

#### **🛠️ Installation**

##### **Windows**
```powershell
# Official installer
# Download from: https://git-scm.com/download/win

# Chocolatey
choco install git

# Winget
winget install Git.Git
```

##### **macOS**
```bash
# Xcode Command Line Tools (includes Git)
xcode-select --install

# Homebrew
brew install git

# MacPorts
sudo port install git
```

##### **Linux (Ubuntu/Debian)**
```bash
# Package manager
sudo apt update
sudo apt install git

# Build from source (latest version)
sudo apt install make libssl-dev libghc-zlib-dev libcurl4-gnutls-dev libxml2-dev libffi-dev
wget https://github.com/git/git/archive/v2.43.0.tar.gz
tar -xzf v2.43.0.tar.gz
cd git-2.43.0
make all
sudo make install
```

#### **⚙️ Configuration**
```bash
# Global configuration
git config --global user.name "Your Name"
git config --global user.email "your.email@company.com"
git config --global init.defaultBranch main

# SSH key generation
ssh-keygen -t ed25519 -C "your.email@company.com"

# Add to SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Test connection
ssh -T git@github.com
```

#### **🧪 Testing**
```bash
# Create test repository
mkdir test-repo
cd test-repo
git init
echo "# UltraCube DevOps Test" > README.md
git add README.md
git commit -m "Initial commit"

# Check status
git status
git log --oneline
```

---

### **2. GitHub Actions**

#### **📖 Overview**
Native CI/CD platform integrated with GitHub for automated workflows.

#### **🛠️ Setup**
GitHub Actions runs in the cloud - no local installation required.

#### **⚙️ Configuration**
```yaml
# .github/workflows/ci.yml
name: UltraCube CI Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '18'
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run tests
      run: npm test
    
    - name: Build application
      run: npm run build

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Deploy to staging
      run: echo "Deploying to staging environment"
```

---

### **3. Jenkins**

#### **📖 Overview**
Open-source automation server for building continuous integration and delivery pipelines.

#### **🛠️ Installation**

##### **Docker (Recommended)**
```bash
# Pull Jenkins image
docker pull jenkins/jenkins:lts

# Run Jenkins container
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts

# Get initial admin password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

##### **Linux (Ubuntu/Debian)**
```bash
# Add Jenkins repository
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

# Install Jenkins
sudo apt update
sudo apt install openjdk-11-jdk
sudo apt install jenkins

# Start Jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

#### **⚙️ Configuration**
```groovy
// Jenkinsfile
pipeline {
    agent any
    
    environment {
        NODE_VERSION = '18'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'npm ci'
            }
        }
        
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
        
        stage('Build') {
            steps {
                sh 'npm run build'
            }
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'echo "Deploying to production"'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
```

---

## 📦 **Containerization**

### **4. Docker**

#### **📖 Overview**
Platform for developing, shipping, and running applications in containers.

#### **🛠️ Installation**

##### **Windows**
```powershell
# Docker Desktop
# Download from: https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe

# Chocolatey
choco install docker-desktop
```

##### **macOS**
```bash
# Docker Desktop
# Download from: https://desktop.docker.com/mac/main/amd64/Docker.dmg

# Homebrew
brew install --cask docker
```

##### **Linux (Ubuntu/Debian)**
```bash
# Remove old versions
sudo apt remove docker docker-engine docker.io containerd runc

# Install dependencies
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release

# Add Docker repository
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io

# Add user to docker group
sudo usermod -aG docker $USER
```

#### **⚙️ Configuration**
```bash
# Start Docker service (Linux)
sudo systemctl start docker
sudo systemctl enable docker

# Configure Docker daemon
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<EOF
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
EOF

sudo systemctl restart docker
```

#### **🧪 Testing**
```bash
# Test Docker installation
docker --version
docker run hello-world

# Build sample application
cat <<EOF > Dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
EOF

# Build and run
docker build -t ucube-app .
docker run -p 3000:3000 ucube-app
```

---

### **5. Podman**

#### **📖 Overview**
Daemonless container engine as an alternative to Docker, with rootless containers.

#### **🛠️ Installation**

##### **Linux (Ubuntu/Debian)**
```bash
# Ubuntu 20.04+
sudo apt update
sudo apt install podman

# For older versions, add repository
. /etc/os-release
echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_${VERSION_ID}/ /" | sudo tee /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list
curl -L https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_${VERSION_ID}/Release.key | sudo apt-key add -
sudo apt update
sudo apt install podman
```

##### **macOS**
```bash
# Homebrew
brew install podman

# Initialize Podman machine
podman machine init
podman machine start
```

#### **🧪 Testing**
```bash
# Test Podman
podman --version
podman run hello-world

# Run rootless container
podman run -d --name nginx-test -p 8080:80 nginx:alpine
```

---

## ⚙️ **Orchestration**

### **6. Kubernetes (kubectl)**

#### **📖 Overview**
Container orchestration platform for automating deployment, scaling, and management.

#### **🛠️ Installation**

##### **kubectl (Kubernetes CLI)**
```bash
# Linux
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# macOS
brew install kubectl

# Windows
choco install kubernetes-cli
```

##### **Local Kubernetes Clusters**

**Minikube (Learning)**
```bash
# Linux
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x minikube
sudo mv minikube /usr/local/bin/

# macOS
brew install minikube

# Start cluster
minikube start
```

**Kind (Kubernetes in Docker)**
```bash
# Install Kind
go install sigs.k8s.io/kind@latest

# Or download binary
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

# Create cluster
kind create cluster --name ucube-cluster
```

#### **⚙️ Configuration**
```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ucube-app
  labels:
    app: ucube-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ucube-app
  template:
    metadata:
      labels:
        app: ucube-app
    spec:
      containers:
      - name: ucube-app
        image: nginx:1.21
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: ucube-service
spec:
  selector:
    app: ucube-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer
```

#### **🧪 Testing**
```bash
# Apply configuration
kubectl apply -f deployment.yaml

# Check deployment
kubectl get deployments
kubectl get pods
kubectl get services

# Scale deployment
kubectl scale deployment ucube-app --replicas=5

# Check logs
kubectl logs -l app=ucube-app
```

---

## 🏗️ **Infrastructure as Code**

### **7. Terraform**

#### **📖 Overview**
Open-source infrastructure as code tool for provisioning and managing cloud resources.

#### **🛠️ Installation**

##### **Linux (Ubuntu/Debian)**
```bash
# Add HashiCorp repository
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update
sudo apt install terraform
```

##### **macOS**
```bash
# Homebrew
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

##### **Windows**
```powershell
# Chocolatey
choco install terraform

# Scoop
scoop install terraform
```

#### **⚙️ Configuration**
```hcl
# main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

resource "aws_vpc" "ucube_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "UltraCube VPC"
  }
}

resource "aws_internet_gateway" "ucube_igw" {
  vpc_id = aws_vpc.ucube_vpc.id

  tags = {
    Name = "UltraCube IGW"
  }
}

output "vpc_id" {
  value = aws_vpc.ucube_vpc.id
}
```

#### **🧪 Testing**
```bash
# Initialize Terraform
terraform init

# Validate configuration
terraform validate

# Plan changes
terraform plan

# Apply changes
terraform apply

# Destroy resources
terraform destroy
```

---

### **8. Ansible**

#### **📖 Overview**
Agentless automation platform for configuration management, application deployment, and orchestration.

#### **🛠️ Installation**

##### **Linux (Ubuntu/Debian)**
```bash
# Package manager
sudo apt update
sudo apt install ansible

# Or via pip
pip3 install ansible
```

##### **macOS**
```bash
# Homebrew
brew install ansible

# Or via pip
pip3 install ansible
```

#### **⚙️ Configuration**
```yaml
# inventory.yml
all:
  hosts:
    web1:
      ansible_host: 192.168.1.10
      ansible_user: ubuntu
    web2:
      ansible_host: 192.168.1.11
      ansible_user: ubuntu
  children:
    webservers:
      hosts:
        web1:
        web2:

# playbook.yml
---
- name: Configure web servers
  hosts: webservers
  become: yes
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: yes

    - name: Start nginx service
      systemd:
        name: nginx
        state: started
        enabled: yes

    - name: Copy website content
      copy:
        content: |
          <html>
            <head><title>UltraCube</title></head>
            <body><h1>Welcome to UltraCube!</h1></body>
          </html>
        dest: /var/www/html/index.html
```

#### **🧪 Testing**
```bash
# Test connectivity
ansible all -m ping -i inventory.yml

# Run playbook
ansible-playbook -i inventory.yml playbook.yml

# Run ad-hoc commands
ansible webservers -a "uptime" -i inventory.yml
```

---

## 📊 **Monitoring & Observability**

### **9. Prometheus**

#### **📖 Overview**
Open-source monitoring and alerting toolkit with powerful query language.

#### **🛠️ Installation**

##### **Docker (Recommended)**
```bash
# Create configuration
mkdir -p prometheus
cat <<EOF > prometheus/prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
  
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
EOF

# Run Prometheus
docker run -d \
  --name prometheus \
  -p 9090:9090 \
  -v $(pwd)/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
```

##### **Binary Installation (Linux)**
```bash
# Download Prometheus
wget https://github.com/prometheus/prometheus/releases/download/v2.47.0/prometheus-2.47.0.linux-amd64.tar.gz
tar xzf prometheus-2.47.0.linux-amd64.tar.gz
cd prometheus-2.47.0.linux-amd64/

# Run Prometheus
./prometheus --config.file=prometheus.yml
```

---

### **10. Grafana**

#### **📖 Overview**
Open-source analytics and interactive visualization platform.

#### **🛠️ Installation**

##### **Docker (Recommended)**
```bash
# Run Grafana
docker run -d \
  --name grafana \
  -p 3000:3000 \
  -e "GF_SECURITY_ADMIN_PASSWORD=admin" \
  grafana/grafana
```

##### **Linux (Ubuntu/Debian)**
```bash
# Add Grafana repository
sudo apt install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -

# Install Grafana
sudo apt update
sudo apt install grafana

# Start Grafana
sudo systemctl enable grafana-server
sudo systemctl start grafana-server
```

#### **⚙️ Configuration**
```json
# datasource.json
{
  "name": "Prometheus",
  "type": "prometheus",
  "url": "http://localhost:9090",
  "access": "proxy",
  "isDefault": true
}
```

---

## 🔄 **Additional DevOps Tools**

### **11. Helm (Kubernetes Package Manager)**

#### **🛠️ Installation**
```bash
# Linux
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# macOS
brew install helm

# Windows
choco install kubernetes-helm
```

#### **🧪 Testing**
```bash
# Add repository
helm repo add bitnami https://charts.bitnami.com/bitnami

# Install application
helm install my-app bitnami/nginx

# List installations
helm list
```

---

### **12. Vagrant**

#### **📖 Overview**
Tool for building and managing virtual machine environments.

#### **🛠️ Installation**
```bash
# Linux (Ubuntu/Debian)
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt update
sudo apt install vagrant

# macOS
brew install vagrant

# Windows
choco install vagrant
```

#### **⚙️ Configuration**
```ruby
# Vagrantfile
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.network "private_network", ip: "192.168.33.10"
  
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
  end
  
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y docker.io
    usermod -aG docker vagrant
  SHELL
end
```

---

## 📋 **Complete DevOps Toolkit Setup**

### **Essential Tools Checklist**

#### **Beginner Level**
- [ ] Git & GitHub/GitLab
- [ ] Docker
- [ ] Basic CI/CD (GitHub Actions or Jenkins)
- [ ] Text editor with DevOps plugins

#### **Intermediate Level**
- [ ] Kubernetes (kubectl + local cluster)
- [ ] Terraform or Ansible
- [ ] Monitoring basics (Prometheus + Grafana)
- [ ] Container registry setup

#### **Advanced Level**
- [ ] Multi-cloud Terraform
- [ ] Advanced Kubernetes (Helm, operators)
- [ ] Comprehensive monitoring stack
- [ ] Security tools integration

### **Environment Setup Script**
```bash
#!/bin/bash
# ucube-devops-setup.sh

echo "🚀 UltraCube DevOps Environment Setup"

# Update system
sudo apt update && sudo apt upgrade -y

# Install Git
sudo apt install -y git

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo usermod -aG docker $USER

# Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# Install Terraform
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform

# Install Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

echo "✅ DevOps tools installation complete!"
echo "Please logout and login again for Docker group membership to take effect."
```

---

## 🚨 **Troubleshooting Guide**

### **Common Issues & Solutions**

#### **Docker Permission Issues (Linux)**
```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Apply changes immediately
newgrp docker

# Test Docker access
docker run hello-world
```

#### **Kubernetes Connection Issues**
```bash
# Check cluster status
kubectl cluster-info

# Reset kubectl config
kubectl config unset current-context

# List available contexts
kubectl config get-contexts
```

#### **Terraform State Issues**
```bash
# Check state
terraform state list

# Refresh state
terraform refresh

# Import existing resource
terraform import aws_instance.example i-1234567890abcdef0
```

#### **Jenkins Plugin Issues**
```bash
# Update plugins via CLI
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin git

# Safe restart
java -jar jenkins-cli.jar -s http://localhost:8080/ safe-restart
```

---

## 📚 **Learning Resources**

### **Official Documentation**
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Terraform Documentation](https://terraform.io/docs)
- [Ansible Documentation](https://docs.ansible.com/)
- [Prometheus Documentation](https://prometheus.io/docs/)

### **Best Practices**
- **Infrastructure as Code**: Version everything
- **CI/CD**: Automate testing and deployment
- **Monitoring**: Implement comprehensive observability
- **Security**: Scan containers and infrastructure
- **Documentation**: Maintain runbooks and procedures

---

<div align="center">

## 🎓 **Ready to Automate Everything?**

Your DevOps toolkit is now ready! These tools will support you through continuous integration, deployment automation, and infrastructure management in our comprehensive curriculum.

![DevOps Success](https://via.placeholder.com/600x100/FF6B35/FFFFFF?text=DevOps+Environment+Ready)

**Need help?** Check our [troubleshooting guide](#-troubleshooting-guide) or [contact our team](mailto:education@ucubetech.com)!

</div>

---

**Created by UltraCube DevOps Engineering Team** | [ucubetech.com](https://www.ucubetech.com) | **Copyright © 2025 UltraCube Technology**
