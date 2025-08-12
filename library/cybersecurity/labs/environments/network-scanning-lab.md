# Lab Environment: Basic Network Scanning

This lab provides a safe environment to practice network reconnaissance techniques.

## Prerequisites

- Docker installed
- Basic command line knowledge
- Completed Foundations modules 1-3

## Lab Setup

### 1. Start the Lab Environment

```bash
# Clone the lab repository
git clone https://github.com/your-org/lab-network-scanning.git
cd lab-network-scanning

# Start the lab environment
docker-compose up -d
```

### 2. Access the Lab

- Target Network: 192.168.100.0/24
- Scanning Host: 192.168.100.10
- Web Interface: <http://localhost:8080>

## Exercises

### Exercise 1: Network Discovery

Use `nmap` to discover active hosts on the network:

```bash
nmap -sn 192.168.100.0/24
```

**Expected Results:** 5-7 active hosts

### Exercise 2: Port Scanning

Scan for open ports on discovered hosts:

```bash
nmap -sT 192.168.100.20-25
```

**Expected Results:** Various services on different ports

### Exercise 3: Service Identification

Identify services running on open ports:

```bash
nmap -sV 192.168.100.20
```

**Expected Results:** HTTP, SSH, FTP services

## Lab Objectives

- Understand network discovery techniques
- Practice safe scanning methodologies
- Identify common network services
- Document findings systematically

## Cleanup

```bash
docker-compose down
docker system prune -f
```

## Troubleshooting

### Common Issues

1. **Docker not starting**: Check Docker daemon status
2. **Network connectivity**: Verify port forwarding
3. **Permission errors**: Run with appropriate privileges

### Getting Help

- Check the lab forum
- Contact lab administrators
- Review documentation
