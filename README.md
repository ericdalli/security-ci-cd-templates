# Security CI/CD Templates

This repository contains example CI/CD pipeline configurations for integrating security controls into software delivery workflows.

All examples are simplified versions of patterns used in real-world environments:
- Dependency and vulnerability scanning
- Secret detection
- Basic SAST checks
- Terraform and IaC validation

---

## 🚀 What’s Included

### 1. GitHub Actions Workflows (`.github/workflows/`)
- `security-scan.yml`  
  - Runs on every push and pull request  
  - Example jobs:
    - Python dependency scan  
    - Secret scanning (simple pattern-based)  
    - Terraform format & validate

*(GitLab CI and other platforms can easily be adapted from the same logic.)*

---

## 🧩 Example Use Cases

- Add quick security checks to an existing repository
- Demonstrate DevSecOps practices in interviews
- Use as a starting point to build more advanced pipelines

---

## 🛠 Requirements

Depending on which parts you use:
- Python 3.9+
- `pip` available in the runner
- `terraform` installed (for IaC examples)

---

## 📌 Notes

These templates are intentionally minimal and vendor-neutral, designed to show **how you think about security in pipelines**, not to replace full enterprise tooling.

---

### 📝 Update Log
- Initial version with pipelines, security scans, and Terraform baseline (2025-01)
