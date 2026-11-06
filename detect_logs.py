from datetime import datetime
failed_count = 0

with open("sample_ssh.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            failed_count += 1

print("CloudSentinel SSH Log Analysis")
print("-----------------------------")
print("Failed login attempts:", failed_count)

if failed_count >= 5:
    severity = "HIGH"
elif failed_count >= 3:
    severity = "MEDIUM"
else:
    severity = "LOW"

print("Severity:", severity)

if severity == "HIGH":
    print("ALERT: Critical suspicious SSH activity!")
elif severity == "MEDIUM":
    print("ALERT: Suspicious SSH activity detected!")
else:
    print("Status: Normal")

report = f"""
CloudSentinel Security Report
-----------------------------
Failed login attempts: {failed_count}
Severity: {severity}
"""

with open("detection_report.txt", "w") as report_file:
    report_file.write(report)

print("Report saved to detection_report.txt")
