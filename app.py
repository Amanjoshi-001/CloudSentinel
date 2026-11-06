from datetime import datetime

🛡️ CloudSentinel — AWS Cloud Security Monitoring

📌 Project Overview

CloudSentinel is a beginner-friendly AWS cloud security monitoring project built using Python and Amazon EC2.

The project monitors SSH authentication activity on a Linux server, detects failed login attempts, classifies security events based on severity, and generates security reports.

It demonstrates practical cloud security concepts, Linux log monitoring, Python automation, and GitHub version control.



project_name = "CloudSentinel"

def detect_severity(failed_attempts):
    if failed_attempts >= 5:
        return "HIGH"
    elif failed_attempts >= 3:
        return "MEDIUM"
    else:
        return "LOW"

security_events = [
    {"source_ip": "192.168.1.100", "failed_attempts": 2},
    {"source_ip": "10.0.0.25", "failed_attempts": 3},
    {"source_ip": "203.0.113.50", "failed_attempts": 7}
]

event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("=== CloudSentinel Security Report ===")
print("Project:", project_name)
print("Event Time:", event_time)

for event in security_events:
    severity = detect_severity(event["failed_attempts"])

    print("------------------------------")
    print("Source IP:", event["source_ip"])
    print("Failed Attempts:", event["failed_attempts"])
    print("Severity:", severity)

with open("/home/ec2-user/CloudSentinel/security_report.txt", "w") as report:
    report.write("=== CloudSentinel Security Report ===\n")
    report.write(f"Project: {project_name}\n")
    report.write(f"Event Time: {event_time}\n\n")

    for event in security_events:
        severity = detect_severity(event["failed_attempts"])

        report.write("------------------------------\n")
        report.write(f"Source IP: {event['source_ip']}\n")
        report.write(f"Failed Attempts: {event['failed_attempts']}\n")
        report.write(f"Severity: {severity}\n\n")

print("Security report saved successfully!")
