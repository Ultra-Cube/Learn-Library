# Installation Guide

Welcome to the Learn-Library installation guide. This document will help you set up the educational platform for local development, contribution, or self-hosted deployment.

## Quick Start

### Prerequisites

Before installing Learn-Library, ensure you have the following:

- **Git** (version 2.20 or higher)
- **Node.js** (version 18 or higher) - for development tools
- **Python** (version 3.8 or higher) - for scripts and automation
- **Docker** (optional) - for containerized development
- **Text Editor** - VS Code, Sublime Text, or your preferred editor

### Basic Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ultra-Cube/Learn-Library.git
   cd Learn-Library
   ```

2. **Install dependencies** (if using development tools)
   ```bash
   npm install
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   python scripts/validate_lessons.py
   ```

4. **Start learning!** Open any lesson file in your preferred editor or browser.

## Installation Methods

### Method 1: Direct Access (Recommended for Learners)

**Best for**: Students, self-learners, casual browsing

```bash
# Clone and start learning immediately
git clone https://github.com/Ultra-Cube/Learn-Library.git
cd Learn-Library
```

**What you get**:
- Immediate access to all lessons
- Offline reading capability
- No setup required
- Full lesson content in Markdown format

### Method 2: Development Setup (For Contributors)

**Best for**: Contributors, content creators, platform developers

```bash
# Clone the repository
git clone https://github.com/Ultra-Cube/Learn-Library.git
cd Learn-Library

# Install Node.js dependencies
npm install

# Install Python dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install

# Verify everything works
npm run test
python scripts/validate_lessons.py
```

**What you get**:
- Full development environment
- Linting and validation tools
- Pre-commit hooks for quality assurance
- Testing and CI/CD integration
- Content generation scripts

### Method 3: Docker Setup (Isolated Environment)

**Best for**: Consistent development environment, easy deployment

```bash
# Clone the repository
git clone https://github.com/Ultra-Cube/Learn-Library.git
cd Learn-Library

# Build the development container
docker build -t learn-library:dev .

# Run the container
docker run -it -v $(pwd):/workspace learn-library:dev

# Or use docker-compose for full stack
docker-compose up -d
```

**What you get**:
- Isolated development environment
- All dependencies pre-installed
- Consistent setup across machines
- Easy deployment and scaling
- Built-in development server

### Method 4: Static Site Generation

**Best for**: Hosting your own instance, custom deployments

```bash
# Install static site generator
npm install -g @11ty/eleventy

# Clone and setup
git clone https://github.com/Ultra-Cube/Learn-Library.git
cd Learn-Library

# Generate static site
eleventy --input=library --output=_site

# Serve locally
eleventy --serve
```

**What you get**:
- Complete static website
- Search functionality
- Responsive design
- Custom branding options
- Easy hosting on any platform

## Platform-Specific Instructions

### Windows

```powershell
# Install Git for Windows
winget install --id Git.Git -e --source winget

# Install Node.js
winget install OpenJS.NodeJS

# Install Python
winget install Python.Python.3.11

# Clone and setup
git clone https://github.com/Ultra-Cube/Learn-Library.git
cd Learn-Library
npm install
pip install -r requirements.txt
```

### macOS

```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install git node python@3.11

# Clone and setup
git clone https://github.com/Ultra-Cube/Learn-Library.git
cd Learn-Library
npm install
pip3 install -r requirements.txt
```

### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install dependencies
sudo apt install git nodejs npm python3 python3-pip

# Clone and setup
git clone https://github.com/Ultra-Cube/Learn-Library.git
cd Learn-Library
npm install
pip3 install -r requirements.txt
```

### Linux (Red Hat/CentOS)

```bash
# Install dependencies
sudo dnf install git nodejs npm python3 python3-pip

# Clone and setup
git clone https://github.com/Ultra-Cube/Learn-Library.git
cd Learn-Library
npm install
pip3 install -r requirements.txt
```

## Development Environment Setup

### VS Code Extensions

Install these recommended extensions for the best development experience:

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-vscode.vscode-json",
    "davidanson.vscode-markdownlint",
    "streetsidesoftware.code-spell-checker",
    "esbenp.prettier-vscode",
    "ms-vscode.live-server"
  ]
}
```

### Environment Configuration

Create a `.env` file for local development:

```bash
# Copy the example environment file
cp .env.example .env

# Edit with your preferences
nano .env
```

Example `.env` content:

```bash
# Development settings
NODE_ENV=development
PORT=3000

# API settings (if using backend features)
API_URL=http://localhost:3001
DATABASE_URL=mongodb://localhost:27017/learn-library

# Feature flags
ENABLE_ANALYTICS=false
ENABLE_COMMENTS=true
ENABLE_PROGRESS_TRACKING=true

# Content settings
DEFAULT_LANGUAGE=en
CONTENT_CACHE_TTL=3600
```

## Verification and Testing

### Validate Installation

```bash
# Check if all lessons are properly formatted
python scripts/validate_lessons.py

# Generate lesson index
python scripts/generate_index.py

# Run content quality checks
npm run lint:content

# Test all code examples
npm run test:examples
```

### Performance Testing

```bash
# Test lesson loading performance
npm run test:performance

# Validate all external links
npm run test:links

# Check image optimization
npm run test:images
```

## Customization Options

### Theme Customization

```bash
# Copy default theme
cp -r themes/default themes/custom

# Edit theme files
nano themes/custom/styles.css
nano themes/custom/config.json

# Apply custom theme
echo "THEME=custom" >> .env
```

### Content Customization

```bash
# Create custom lesson structure
mkdir -p custom-content/my-domain/foundations

# Copy lesson template
cp templates/lesson-template.md custom-content/my-domain/foundations/

# Add to content index
python scripts/add_custom_content.py custom-content/
```

## Troubleshooting

### Common Issues

**Issue**: Node.js version conflicts
```bash
# Solution: Use Node Version Manager
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 18
nvm use 18
```

**Issue**: Permission errors on Linux/macOS
```bash
# Solution: Fix npm permissions
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.profile
source ~/.profile
```

**Issue**: Python package conflicts
```bash
# Solution: Use virtual environment
python -m venv learn-library-env
source learn-library-env/bin/activate  # On Windows: learn-library-env\Scripts\activate
pip install -r requirements.txt
```

**Issue**: Git submodule errors
```bash
# Solution: Initialize submodules
git submodule init
git submodule update
```

### Performance Optimization

```bash
# Clear npm cache
npm cache clean --force

# Clear Python cache
find . -type d -name __pycache__ -delete

# Optimize images
npm run optimize:images

# Compress content
npm run compress:content
```

### Getting Help

If you encounter issues during installation:

1. **Check the FAQ**: [docs/FAQ.md](docs/FAQ.md)
2. **Search issues**: [GitHub Issues](https://github.com/Ultra-Cube/Learn-Library/issues)
3. **Ask for help**: [GitHub Discussions](https://github.com/Ultra-Cube/Learn-Library/discussions)
4. **Contact maintainers**: See [SUPPORT.md](SUPPORT.md)

## Next Steps

After successful installation:

1. **Explore the content**: Start with [docs/INDEX.md](docs/INDEX.md)
2. **Choose a learning path**: See [library/README.md](library/README.md)
3. **Set up your development environment**: Follow the guides in each domain
4. **Join the community**: Participate in discussions and contribute
5. **Track your progress**: Use the progress tracking templates

## Updates and Maintenance

### Staying Up to Date

```bash
# Pull latest changes
git pull origin main

# Update dependencies
npm update
pip install -r requirements.txt --upgrade

# Validate after updates
python scripts/validate_lessons.py
npm run test
```

### Automated Updates

Enable automatic updates by setting up a cron job:

```bash
# Edit crontab
crontab -e

# Add weekly update check (runs Sundays at 2 AM)
0 2 * * 0 cd /path/to/Learn-Library && git pull origin main && npm update
```

---

**Congratulations!** You now have Learn-Library installed and ready to use. Happy learning! 🚀

For questions or support, please see our [Support Guide](SUPPORT.md) or open an issue on GitHub.
