import subprocess
import re
from collections import defaultdict
from datetime import datetime

print("CloudSentinel Live IP Detector")
print("--------------------------------")

command = [
    "sudo",
    "journalctl",
    "-u", "sshd",
    "--since", "24 hours ago",
    "--no-pager"
]

result = subprocess.run(
    command,
    capture_output=True,
    text=True
)

logs = result.stdout
failed_ips = defaultdict(int)

for line in logs.splitlines():
    if "Failed password" in line:
        match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

        if match:
            ip = match.group(1)
            failed_ips[ip] += 1

print("\nFailed Login Attempts by IP:")

for ip, count in failed_ips.items():
    print(f"{ip}: {count} failed attempts")

    if count >= 3:
        print(f"ALERT: Suspicious activity from {ip}!")

report = f"""
CloudSentinel Live IP Security Report
Timestamp: {datetime.now()}
------------------------------------
"""

if failed_ips:
    for ip, count in failed_ips.items():
        report += f"{ip}: {count} failed attempts\n"

        if count >= 3:
            report += f"ALERT: Suspicious activity from {ip}!\n"
else:
    report += "No failed SSH login attempts detected.\n"

with open("live_ip_report.txt", "w") as file:
    file.write(report)

print("\nReport saved to live_ip_report.txt")
