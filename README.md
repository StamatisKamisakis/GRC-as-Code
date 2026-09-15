# GRC-as-Code (Governance, Risk, and Compliance) 🚀

Welcome to the **GRC-as-Code** repository! This project is a curated collection of automated scripts, configurations, and tools designed to bridge the gap between IT regulatory compliance (ISO, NIST, SOC2) and software engineering. 

The goal of this repository is to demonstrate how organizations can automate auditing, enforce safety thresholds, and maintain robust audit trails continuously rather than relying on manual, periodic checks.

---

## 🛠️ Project Structure

Currently, the repository contains the following modules:

### 1. Automated System Resource & Model Monitoring
* **Directory / Script:** `Automated System Resource & Model Monitoring`
* **Standard Aligned:** **ISO/IEC 42001 (AI Management System) - Control A.6.2 (AI System Performance Baseline)**
* **Description:** A Python-based monitoring utility for Linux environments that tracks system telemetry (CPU and RAM consumption). It automatically assesses whether the host infrastructure complies with corporate risk thresholds and securely streams tamper-evident compliance audit logs straight to the Linux Syslog (`journalctl`).

*(More GRC automations coming soon!)*

---

## 🚀 Getting Started

### Prerequisites
To run the automated scripts, ensure you have Python 3.x installed along with the required dependencies:

```bash
pip install psutil
```

### Running the Monitoring Module
Navigate to the module directory and execute the script with appropriate privileges (required for Syslog access on certain Linux configurations):

```bash
python3 main.py
```

---

## 📊 Key Use Cases Covered
* **Continuous Compliance:** Moving away from static spreadsheets to real-time, event-driven auditing.
* **Traceability & Audit Trails:** Securely logging policy violations into system daemons to satisfy rigorous third-party auditor checks.
* **AI Safety Thresholds:** Proactively catching rogue, over-utilizing AI models or loops before they breach operational metrics.

---

## 🗺️ Roadmap & Future Projects
I am actively developing this repository to include broader GRC-as-code automation frameworks, such as:
- [ ] **ISO 27001 Access Control Auditing:** Automated detection of stale SSH keys or unauthorized sudo users.
- [ ] **Infrastructure-as-Code (IaC) Scanning:** Automated compliance checks for Terraform configurations.
- [ ] **NIST SP 800-53 Benchmarking:** Scripts to automatically check OS hardening configurations.

---

## 🤝 Contributing
Contributions, issue reports, and feature ideas are more than welcome! Feel free to open an issue or submit a pull request if you want to extend these compliance automation tools.

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
