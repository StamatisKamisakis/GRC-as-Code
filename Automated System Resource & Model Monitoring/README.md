# Module: Automated System Resource & Model Monitoring 🛡️

This module provides a lightweight, automated compliance logging mechanism tailored for AI infrastructure. It is designed to satisfy the strict continuous monitoring and audit trail requirements introduced by **ISO/IEC 42001 (Artificial Intelligence Management System)**.

---

## 📋 ISO/IEC 42001 Mapping

* **Control Domain:** A.6 - Resource Management & System Performance
* **Specific Control:** **A.6.2 (AI System Performance Baseline)**
* **Objective:** Organizations must establish performance baselines for AI systems, monitor deviations, and maintain immutable logs to ensure transparency, accountability, and traceability (Audit Trail).

---

## ⚙️ How It Works

The core script (`ai_system_monitor.py`) hooks directly into the host operating system to capture real-time resource utilization. 

1. **Telemetry Gathering:** Uses the `psutil` library to poll CPU and virtual memory (RAM) usage intervals.
2. **Policy Enforcement:** Evaluates telemetry metrics against pre-defined corporate risk thresholds (`MAX_CPU_PERCENT`, `MAX_RAM_PERCENT`).
3. **Compliance Logging:** 
   * If metrics are within bounds, a `[PASS]` token is registered.
   * If thresholds are breached, a `[ALERT]` token triggers a `NON-COMPLIANT` event.
4. **Tamper-Evident Auditing:** All compliance states are routed directly to the native Linux **Syslog daemon** (`/dev/log` or `/var/run/syslog`). This ensures that logs are structured, centralized, and decoupled from the application layer to mitigate tampering risks.

---

## 🚀 Configuration & Deployment

### Customizing Thresholds
You can easily adjust the compliance thresholds at the top of the `ai_system_monitor.py` script to match your hardware profile:

```python
MAX_CPU_PERCENT = 85.0   # Adjust based on your peak AI inference loads
MAX_RAM_PERCENT = 90.0   # Adjust based on large language model (LLM) caching
```

### Execution
Run the script manually to perform a point-in-time compliance check:

```bash
python3 ai_system_monitor.py
```

### Production Recommendation (Automation via Cron)
To ensure continuous compliance auditing as mandated by ISO 42001, deploy the script as a recurring cron job. For example, to audit system state every 5 minutes:

```bash
*/5 * * * * /usr/bin/python3 /path/to/GRC-as-Code/Automated\ System\ Resource\ &\ Model\ Monitoring/ai_system_monitor.py > /dev/null 2>&1
```

---

## 📸 Proof of Concept / Execution Baseline

Here is the tool running live on an Ubuntu environment, validating system thresholds and recording audit events to `journalctl`:

*(Insert your screenshot/gif below)*

---

## 🛠️ Dependencies
* **Python 3.x**
* **psutil** (Cross-platform process and system utilities)
