#!/usr/bin/env python3
import os
import sys
import logging
import logging.handlers
import psutil

# ---------------------------------------------------------
# ISO 42001 Control A.6.2 - AI System Performance Baseline
# ---------------------------------------------------------
# Security Policy Thresholds
MAX_CPU_PERCENT = 85.0   # Maximum allowed CPU usage (%)
MAX_RAM_PERCENT = 90.0   # Maximum allowed RAM usage (%)

def setup_syslog_logger():
    """
    Configures Python syslog integration for Linux systemd/journalctl
    to maintain an immutable ISO audit trail (Traceability).
    """
    logger = logging.getLogger("ISO42001-Monitor")
    logger.setLevel(logging.INFO)
    
    # Identify the appropriate Linux syslog socket
    syslog_address = '/dev/log' if os.path.exists('/dev/log') else '/var/run/syslog'
    
    try:
        handler = logging.handlers.SysLogHandler(address=syslog_address)
        formatter = logging.Formatter('%(name)s[%(process)d]: %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    except Exception as e:
        print(f"[!] Warning: Could not connect to syslog ({e}). Falling back to stdout.")
        logging.basicConfig(level=logging.INFO)
        
    return logger

def check_ai_system_health(logger):
    """
    Collects system performance metrics and verifies ISO 42001 compliance thresholds.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    
    compliance_status = "COMPLIANT"
    violations = []

    # CPU threshold evaluation
    if cpu_usage > MAX_CPU_PERCENT:
        compliance_status = "NON-COMPLIANT"
        violations.append(f"High CPU Usage: {cpu_usage}% (Limit: {MAX_CPU_PERCENT}%)")

    # RAM threshold evaluation
    if ram_usage > MAX_RAM_PERCENT:
        compliance_status = "NON-COMPLIANT"
        violations.append(f"High RAM Usage: {ram_usage}% (Limit: {MAX_RAM_PERCENT}%)")

    # Construct log payload
    log_payload = f"Control A.6.2 Check | Status: {compliance_status} | CPU: {cpu_usage}% | RAM: {ram_usage}%"

    if compliance_status == "COMPLIANT":
        logger.info(f"[PASS] {log_payload}")
        print(f"✅ {log_payload}")
    else:
        details = " | ".join(violations)
        logger.warning(f"[ALERT] {log_payload} | Violations: {details}")
        print(f"⚠️ [NON-COMPLIANT] {log_payload}")
        print(f"   Details: {details}")

if __name__ == "__main__":
    logger = setup_syslog_logger()
    check_ai_system_health(logger)
