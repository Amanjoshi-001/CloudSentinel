from datetime import datetime
from collections import defaultdict
import re

failed_count = 0
ip_attempts = defaultdict(int)

with open("sample_ssh.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            failed_count += 1

            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

            if match:
                source_ip = match.group(1)
                ip_attempts[source_ip] += 1

print("CloudSentinel SSH Log Analysis")
print("--------------------------------")
print("Failed login attempts:", failed_count)

if failed_count >= 5:
    severity = "HIGH"
elif failed_count >= 3:
    severity = "MEDIUM"
else:
    severity = "LOW"

print("Severity:", severity)

print("\nFailed Login Attempts by IP:")

for ip, count in ip_attempts.items():
    print(f"{ip}: {count} failed attempts")

    if count >= 3:
        print(f"ALERT: Suspicious activity from {ip}!")

report = f"""
CloudSentinel Security Report
-----------------------------
Failed login attempts: {failed_count}
Severity: {severity}

Failed Login Attempts by IP:
"""

for ip, count in ip_attempts.items():
    report += f"{ip}: {count} failed attempts\n"

    if count >= 3:
        report += f"ALERT: Suspicious activity from {ip}!\n"

with open("detection_report.txt", "w") as report_file:
    report_file.write(report)

print("\nReport saved to detection_report.txt")
