# 💻 Software Development Tools Reference

> **UltraCube Learn-Library** | Development Tools & Installation Guide  
> **Maintained by**: UltraCube Development Team  
> **Last Updated**: August 13, 2025

![Development Tools Banner](https://via.placeholder.com/800x150/007ACC/FFFFFF?text=UltraCube+%7C+Development+Tools+Reference)

---

## 🎯 Overview

Comprehensive guide to essential development tools used throughout the UltraCube Learn-Library software development curriculum. This reference covers everything from code editors to deployment tools.

## 🛠️ Code Editors & IDEs

### **Visual Studio Code** - Universal Code Editor

**Description**: Lightweight, extensible code editor with excellent language support.

#### Installation

```bash
# Ubuntu/Debian
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
sudo apt update && sudo apt install code

# macOS
brew install --cask visual-studio-code

# Windows
# Download from: https://code.visualstudio.com/download
```

#### Essential Extensions

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-typescript-next
code --install-extension ms-vscode.vscode-json
code --install-extension ms-toolsai.jupyter
code --install-extension ms-vscode.vscode-eslint
code --install-extension bradlc.vscode-tailwindcss
code --install-extension ms-vscode.vscode-docker
code --install-extension ms-kubernetes-tools.vscode-kubernetes-tools
```

### **JetBrains IDEs** - Professional Development

#### IntelliJ IDEA (Java/Kotlin)

```bash
# Install via Jetbrains Toolbox
# Download from: https://www.jetbrains.com/toolbox-app/

# Ubuntu via Snap
sudo snap install intellij-idea-community --classic

# macOS
brew install --cask intellij-idea-ce
```

#### PyCharm (Python)

```bash
# Community Edition
sudo snap install pycharm-community --classic

# macOS
brew install --cask pycharm-ce
```

---

## 🌐 Web Development Stack

### **Node.js & npm** - JavaScript Runtime

#### Installation

```bash
# Using Node Version Manager (Recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install --lts
nvm use --lts

# Ubuntu/Debian (Direct)
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# macOS
brew install node

# Windows
# Download from: https://nodejs.org/
```

#### Essential Global Packages

```bash
# Package managers
npm install -g yarn pnpm

# Development tools
npm install -g nodemon create-react-app @vue/cli
npm install -g typescript ts-node @angular/cli
npm install -g webpack webpack-cli vite

# Linting and formatting
npm install -g eslint prettier

# Testing
npm install -g jest cypress
```

### **React Development**

```bash
# Create React App
npx create-react-app my-app
cd my-app
npm start

# Vite (Modern alternative)
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install && npm run dev

# Next.js (Full-stack React)
npx create-next-app@latest my-next-app
cd my-next-app
npm run dev
```

### **Vue.js Development**

```bash
# Vue CLI
npm install -g @vue/cli
vue create my-vue-app
cd my-vue-app
npm run serve

# Vite + Vue 3
npm create vue@latest my-vue-app
cd my-vue-app
npm install && npm run dev
```

### **Angular Development**

```bash
# Angular CLI
npm install -g @angular/cli
ng new my-angular-app
cd my-angular-app
ng serve
```

---

## 🐍 Python Development

### **Python Installation & Management**

#### Python Installation

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-venv

# macOS (using Homebrew)
brew install python

# Windows
# Download from: https://www.python.org/downloads/
```

#### Virtual Environment Management

```bash
# Built-in venv
python3 -m venv myenv
source myenv/bin/activate  # Linux/macOS
myenv\Scripts\activate     # Windows

# Conda (Recommended for data science)
# Download Miniconda: https://docs.conda.io/en/latest/miniconda.html
conda create -n myenv python=3.9
conda activate myenv

# Poetry (Modern dependency management)
curl -sSL https://install.python-poetry.org | python3 -
poetry new my-project
cd my-project
poetry install
```

#### Essential Python Packages

```bash
# Web frameworks
pip install django flask fastapi

# Data science
pip install numpy pandas matplotlib seaborn scikit-learn
pip install jupyter notebook jupyterlab

# Machine learning
pip install tensorflow pytorch transformers

# Testing
pip install pytest pytest-cov

# Code quality
pip install black flake8 mypy
```

---

## ☕ Java Development

### **Java Development Kit (JDK)**

```bash
# OpenJDK (Recommended)
# Ubuntu/Debian
sudo apt install openjdk-11-jdk openjdk-17-jdk

# macOS
brew install openjdk@11 openjdk@17

# SDKMAN (Multi-version management)
curl -s "https://get.sdkman.io" | bash
source ~/.sdkman/bin/sdkman-init.sh
sdk install java 17.0.2-open
sdk use java 17.0.2-open
```

### **Build Tools**

#### Maven

```bash
# Ubuntu/Debian
sudo apt install maven

# macOS
brew install maven

# Manual installation
wget https://apache.osuosl.org/maven/maven-3/3.8.6/binaries/apache-maven-3.8.6-bin.tar.gz
tar xzf apache-maven-3.8.6-bin.tar.gz
export PATH=$PATH:/path/to/apache-maven-3.8.6/bin
```

#### Gradle

```bash
# Ubuntu/Debian
sudo apt install gradle

# macOS
brew install gradle

# SDKMAN
sdk install gradle
```

### **Spring Boot Development**

```bash
# Spring Boot CLI
sdk install springboot

# Create new project
spring init --dependencies=web,jpa,h2 my-spring-app
cd my-spring-app
./mvnw spring-boot:run
```

---

## 📱 Mobile Development

### **React Native**

```bash
# Install React Native CLI
npm install -g @react-native-community/cli

# Create new project
npx react-native init MyApp
cd MyApp

# iOS (macOS only)
cd ios && pod install && cd ..
npx react-native run-ios

# Android
npx react-native run-android
```

### **Flutter**

```bash
# macOS installation
# Download Flutter SDK from: https://flutter.dev/docs/get-started/install

# Add to PATH
export PATH="$PATH:`pwd`/flutter/bin"

# Verify installation
flutter doctor

# Create new project
flutter create my_flutter_app
cd my_flutter_app
flutter run
```

### **Android Development**

```bash
# Android Studio
# Download from: https://developer.android.com/studio

# SDK tools via command line
# Download SDK tools and set ANDROID_HOME

# Install platform tools
sdkmanager "platform-tools" "platforms;android-31"
```

---

## 🗄️ Database Tools

### **Database Management**

#### PostgreSQL

```bash
# Ubuntu/Debian
sudo apt install postgresql postgresql-contrib

# macOS
brew install postgresql
brew services start postgresql

# Create database
sudo -u postgres createdb mydb
sudo -u postgres psql mydb
```

#### MySQL

```bash
# Ubuntu/Debian
sudo apt install mysql-server

# macOS
brew install mysql
brew services start mysql

# Secure installation
sudo mysql_secure_installation
```

#### MongoDB

```bash
# Ubuntu/Debian
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
sudo apt update && sudo apt install mongodb-org

# macOS
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb/brew/mongodb-community
```

### **Database GUI Tools**

```bash
# DBeaver (Universal)
# Download from: https://dbeaver.io/download/

# pgAdmin (PostgreSQL)
# Download from: https://www.pgadmin.org/download/

# MySQL Workbench
# Download from: https://www.mysql.com/products/workbench/
```

---

## 🔧 Version Control & Collaboration

### **Git** - Version Control System

#### Installation

```bash
# Ubuntu/Debian
sudo apt install git

# macOS
# Pre-installed or via Homebrew
brew install git

# Windows
# Download from: https://git-scm.com/download/win
```

#### Basic Configuration

```bash
# Set user information
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default editor
git config --global core.editor "code --wait"

# Set default branch name
git config --global init.defaultBranch main

# Useful aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
```

#### Essential Commands

```bash
# Repository management
git init
git clone https://github.com/user/repo.git
git remote add origin https://github.com/user/repo.git

# Basic workflow
git add .
git commit -m "commit message"
git push origin main
git pull origin main

# Branching
git branch feature-branch
git checkout feature-branch
git checkout -b feature-branch  # Create and switch

# Merging
git checkout main
git merge feature-branch
git branch -d feature-branch
```

### **GitHub CLI**

```bash
# Installation
# macOS
brew install gh

# Ubuntu/Debian
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update && sudo apt install gh

# Authentication
gh auth login

# Common commands
gh repo create my-repo
gh repo clone user/repo
gh pr create --title "New feature" --body "Description"
gh pr merge
```

---

## 🐳 Containerization & Orchestration

### **Docker** - Containerization Platform

#### Installation

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update && sudo apt install docker-ce docker-ce-cli containerd.io

# Add user to docker group
sudo usermod -aG docker $USER

# macOS
brew install --cask docker

# Windows
# Download Docker Desktop from: https://www.docker.com/products/docker-desktop
```

#### Essential Commands

```bash
# Container management
docker run -it ubuntu bash
docker ps
docker ps -a
docker stop container_id
docker rm container_id

# Image management
docker images
docker pull nginx
docker build -t my-app .
docker rmi image_id

# Volume and network
docker volume create my-volume
docker network create my-network

# Docker Compose
docker-compose up -d
docker-compose down
docker-compose logs
```

### **Kubernetes** - Container Orchestration

#### kubectl Installation

```bash
# Linux
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# macOS
brew install kubectl

# Windows
# Download from: https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/
```

#### Local Development Clusters

```bash
# Minikube
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube /usr/local/bin/
minikube start

# kind (Kubernetes in Docker)
go install sigs.k8s.io/kind@v0.14.0
kind create cluster

# Docker Desktop (built-in)
# Enable Kubernetes in Docker Desktop settings
```

---

## 🚀 CI/CD & Automation

### **GitHub Actions**

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '16'
    - run: npm install
    - run: npm test
```

### **Jenkins** - Automation Server

```bash
# Ubuntu/Debian
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update && sudo apt install jenkins

# Start Jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins

# Access: http://localhost:8080
```

---

## 🧪 Testing Tools

### **Jest** - JavaScript Testing

```bash
# Installation
npm install --save-dev jest

# Basic test
// sum.test.js
const sum = (a, b) => a + b;
test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});

# Run tests
npm test
```

### **Pytest** - Python Testing

```bash
# Installation
pip install pytest

# Basic test
# test_sum.py
def sum(a, b):
    return a + b

def test_sum():
    assert sum(1, 2) == 3

# Run tests
pytest
```

### **Cypress** - End-to-end Testing

```bash
# Installation
npm install --save-dev cypress

# Open Cypress
npx cypress open

# Run tests
npx cypress run
```

---

## 📊 Monitoring & Debugging

### **Development Tools**

```bash
# Chrome DevTools (built-in)
# Firefox Developer Tools (built-in)

# React Developer Tools
# Install browser extension

# Vue.js DevTools
# Install browser extension

# Postman (API testing)
# Download from: https://www.postman.com/downloads/

# Insomnia (API client)
# Download from: https://insomnia.rest/download
```

---

## 🎯 Learning Path Integration

These tools are integrated throughout our development curriculum:

- **[Web Development Track](../library/software-development/web-development/)**: Frontend and backend tools
- **[Mobile Development Track](../library/software-development/mobile-development/)**: Mobile development frameworks
- **[Backend Development Track](../library/software-development/backend-development/)**: Server-side technologies

## 🆘 Support & Resources

### 📚 **Official Documentation**
- Tool-specific documentation and guides
- Video tutorials in our [docs/video-resources.md](../docs/video-resources.md)
- Community discussions and Q&A

### 🐛 **Issues & Updates**
- Report tool-related issues in our GitHub repository
- Suggest new tools or improvements
- Contribute installation scripts and configurations

---

## 📝 **License & Attribution**

This tool reference guide is part of the **UltraCube Learn-Library** project.

**Created by**: UltraCube Development Team  
**License**: MIT License  
**Website**: [ucubetech.com](https://www.ucubetech.com)

---

*Tools and technologies referenced are trademarks of their respective owners. This guide is for educational purposes only.*
