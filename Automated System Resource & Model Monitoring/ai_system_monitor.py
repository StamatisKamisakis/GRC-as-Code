#!/usr/bin/env python3
import os
import sys
import logging
import logging.handlers
import psutil

# ---------------------------------------------------------
# ISO 42001 Control A.6.2 - AI System Performance Baseline
# ---------------------------------------------------------
# Καθορισμός Ορίων Ασφαλείας (Policy Thresholds)
MAX_CPU_PERCENT = 85.0   # Μέγιστη επιτρεπόμενη χρήση CPU (%)
MAX_RAM_PERCENT = 90.0   # Μέγιστη επιτρεπόμενη χρήση RAM (%)

def setup_syslog_logger():
    """
    Σύνδεση του Python script με το Linux Syslog / journalctl
    για να τηρείται το ISO audit trail (Traceability).
    """
    logger = logging.getLogger("ISO42001-Monitor")
    logger.setLevel(logging.INFO)
    
    # Επιλογή syslog socket ανάλογα με το OS
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
    Συλλογή metrics και έλεγχος συμμόρφωσης με τα όρια.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    
    compliance_status = "COMPLIANT"
    violations = []

    # Έλεγχος CPU
    if cpu_usage > MAX_CPU_PERCENT:
        compliance_status = "NON-COMPLIANT"
        violations.append(f"High CPU Usage: {cpu_usage}% (Limit: {MAX_CPU_PERCENT}%)")

    # Έλεγχος RAM
    if ram_usage > MAX_RAM_PERCENT:
        compliance_status = "NON-COMPLIANT"
        violations.append(f"High RAM Usage: {ram_usage}% (Limit: {MAX_RAM_PERCENT}%)")

    # Καταγραφή Αποτελεσμάτων
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
