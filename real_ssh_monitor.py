from datetime import datetime
import subprocess

print("CloudSentinel Real SSH Monitor")
print("-----------------------------")

command = [
    "sudo",
    "journalctl",
    "-u",
    "sshd",
    "--since",
    "24 hours ago",
    "--no-pager"
]

result = subprocess.run(
    command,
    capture_output=True,
    text=True
)

logs = result.stdout

failed_count = logs.count("Failed password")
accepted_count = logs.count("Accepted publickey")

if failed_count >= 5:
    severity = "HIGH"
elif failed_count >= 3:
    severity = "MEDIUM"
else:
    severity = "LOW"

print("Successful SSH logins:", accepted_count)
print("Failed SSH password attempts:", failed_count)
print("Severity:", severity)

if severity == "HIGH":
    alert_message = "CRITICAL: Suspicious SSH activity detected!"
    print("ALERT:", alert_message)
elif severity == "MEDIUM":
    alert_message = "WARNING: Multiple failed SSH login attempts!"
    print("ALERT:", alert_message)
else:
    alert_message = "NORMAL: No significant suspicious activity."
    print("Status: Normal")

report = f"""
Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
CloudSentinel Real SSH Monitoring Report
---------------------------------------
Successful SSH logins: {accepted_count}
Failed SSH password attempts: {failed_count}
Severity: {severity}
Alert: {alert_message}
"""

with open("real_ssh_report.txt", "w") as report_file:
    report_file.write(report)

print("Report saved to real_ssh_report.txt")
