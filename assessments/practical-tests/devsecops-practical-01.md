---
test_id: devsecops-practical-01
module: module-02-cicd-security-basics
level: beginner
track: devsecops
duration: 60m
passing_score: 80%
---

# Practical Test: CI/CD Security Implementation

## Instructions

This practical test evaluates your ability to implement security controls in a CI/CD pipeline.

**Time Limit**: 60 minutes
**Passing Score**: 80% (24/30 points)
**Resources Allowed**: Documentation, online references
**Tools Provided**: GitHub repository, Actions environment

## Scenario

You are a DevSecOps engineer tasked with securing a CI/CD pipeline for a Node.js web application. The current pipeline lacks security controls and needs to be hardened according to industry best practices.

## Repository Access

- **Repository**: `https://github.com/learn-library/test-nodejs-app`
- **Branch**: `security-test`
- **Access**: Fork the repository to your account

## Tasks

### Task 1: Secret Scanning (10 points)

Implement secret detection in the pipeline to catch hardcoded credentials.

**Requirements**:
- Add a secret scanning step using TruffleHog or similar tool
- Configure the scan to run on every push and pull request
- Ensure the pipeline fails if secrets are detected
- Test with a known secret pattern

**Deliverable**: GitHub Actions workflow file with secret scanning

### Task 2: Static Code Analysis (10 points)

Integrate static application security testing (SAST) into the pipeline.

**Requirements**:
- Add ESLint security plugin or Semgrep for JavaScript analysis
- Configure rules for common security vulnerabilities
- Generate SARIF output for GitHub Security tab
- Set up to fail build on high-severity issues

**Deliverable**: SAST configuration and workflow integration

### Task 3: Dependency Vulnerability Scanning (10 points)

Implement dependency checking to identify vulnerable packages.

**Requirements**:
- Add npm audit or Snyk scanning
- Configure to check both direct and transitive dependencies
- Set threshold for failing build (e.g., high/critical vulnerabilities)
- Generate vulnerability report

**Deliverable**: Dependency scanning workflow step

## Bonus Tasks (Extra Credit)

### Bonus 1: Container Security Scanning (5 points)

If the application uses Docker:
- Add container image vulnerability scanning
- Use tools like Trivy or Clair
- Scan both OS packages and application dependencies

### Bonus 2: Infrastructure as Code (IaC) Scanning (5 points)

If infrastructure files are present:
- Add Terraform/CloudFormation security scanning
- Use tools like Checkov or Terrascan
- Check for misconfigurations and security best practices

## Evaluation Criteria

### Technical Implementation (20 points)

- **Functionality**: Tools run correctly and produce expected results
- **Configuration**: Proper tool configuration for security focus
- **Integration**: Seamless integration with existing pipeline
- **Error Handling**: Appropriate failure modes and error reporting

### Security Coverage (10 points)

- **Completeness**: All required security checks implemented
- **Effectiveness**: Configuration catches real security issues
- **Thresholds**: Appropriate sensitivity for failing builds
- **Reporting**: Clear security findings and recommendations

## Submission Requirements

### 1. Workflow File

Submit your complete `.github/workflows/security.yml` file that includes:
- All required security scanning steps
- Proper job dependencies and conditions
- Artifact uploads for reports
- Appropriate triggers (push, PR, schedule)

### 2. Configuration Files

Include any additional configuration files:
- ESLint security configuration
- Semgrep rules
- Tool-specific config files

### 3. Documentation

Provide a brief README explaining:
- Security tools implemented and why
- How to interpret scan results
- Recommended actions for different finding severities
- Any assumptions or limitations

### 4. Test Results

Include evidence of testing:
- Screenshot of successful pipeline run
- Example of pipeline failing on security issue
- Sample security scan reports

## Sample Solution Structure

```yaml
name: Security Pipeline
on: [push, pull_request]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Secret Scan
        # Your implementation here
        
      - name: SAST Scan
        # Your implementation here
        
      - name: Dependency Check
        # Your implementation here
        
      - name: Upload Results
        # Your implementation here
```

## Common Issues and Tips

### Secret Scanning
- Be careful not to commit real secrets during testing
- Use test patterns or dummy secrets for validation
- Consider using GitHub's built-in secret scanning

### SAST Tools
- Different tools have different strengths
- Consider combining multiple tools for better coverage
- Pay attention to false positive rates

### Dependency Scanning
- npm audit is built into Node.js ecosystem
- Consider both development and production dependencies
- Regular updates of dependency databases are important

## Time Management

- **15 minutes**: Repository setup and understanding
- **15 minutes**: Secret scanning implementation
- **15 minutes**: SAST integration
- **15 minutes**: Dependency scanning setup
- **Bonus time**: Additional features or improvements

## Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [OWASP DevSecOps Guideline](https://owasp.org/www-project-devsecops-guideline/)
- [TruffleHog Documentation](https://github.com/trufflesecurity/trufflehog)
- [Semgrep Rules](https://semgrep.dev/explore)
- [NPM Audit Documentation](https://docs.npmjs.com/cli/v7/commands/npm-audit)

## Submission

1. Create a pull request in your forked repository
2. Include all required files and documentation
3. Submit the PR link through the assessment platform
4. Ensure all pipeline checks pass before submission

Good luck!
