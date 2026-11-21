🛡️ CloudSentinel — AWS Cloud Security Monitoring

📌 Project Overview

CloudSentinel is an AWS cloud security monitoring project built using Python, Amazon EC2, and AWS CloudWatch.

The project monitors SSH authentication activity on a Linux server, detects failed login attempts, identifies suspicious IP activity, and generates security reports.

It also provides a Streamlit dashboard for monitoring security events, CPU utilization, CloudWatch alarm status, and EC2 instance health.

This project demonstrates practical cloud security concepts, Linux log monitoring, Python automation, AWS monitoring services, and GitHub version control.

🛠️ Technologies Used

AWS EC2 — Cloud server hosting

Amazon Linux 2023 — Operating system

AWS CloudWatch — CPU metrics and alarm monitoring

AWS SNS — Email notification integration

Python 3 — Security monitoring and log analysis

Streamlit — Security monitoring dashboard

Boto3 — AWS SDK for Python

Linux SSH and Journal Logs — Authentication event monitoring

Git & GitHub — Version control and project hosting

🚀 Project Features

Analyze sample SSH authentication logs using Python

Detect failed SSH password attempts

Classify security severity as LOW, MEDIUM, or HIGH

Monitor real SSH authentication events from Linux journal logs

Identify failed SSH login attempts by source IP

Generate security monitoring reports

Automatically execute SSH monitoring every 10 seconds

Display security information through a Streamlit dashboard

Monitor AWS EC2 CPU utilization using CloudWatch

Display CloudWatch CPU alarm status

Monitor EC2 instance and system health checks

Configure SNS email notifications for CloudWatch alarm events

📂 Project Structure

CloudSentinel/
├── app.py
├── dashboard.py
├── detect_logs.py
├── live_ip_detector.py
├── real_ssh_monitor.py
├── auto_monitor.py
├── analyze_ssh_history.py
├── cloudwatch_monitor.py
├── sample_ssh.log
├── detection_report.txt
├── README.md
└── .gitignore

Additional monitoring reports and SSH history files are generated when the scripts run.

⚙️ How to Run

1. Activate the Python virtual environment

source dashboard-env/bin/activate

2. Analyze Sample SSH Logs

python3 detect_logs.py

3. Monitor Real SSH Activity

python3 real_ssh_monitor.py

4. Start Automatic SSH Monitoring

python3 auto_monitor.py

The automatic monitor executes the real SSH monitoring script every 10 seconds.

Press Ctrl + C to stop automatic monitoring.

5. Start the Security Dashboard

streamlit run dashboard.py

Open the dashboard through your SSH tunnel at:

http://localhost:8501

6. Run AWS CloudWatch CPU Monitoring

python3 cloudwatch_monitor.py

🚨 Severity Classification

Severity

Failed SSH Password Attempts

LOW

0–2

MEDIUM

3–4

HIGH

5 or more

☁️ AWS Environment

Cloud Provider: Amazon Web Services

Services: EC2, CloudWatch, SNS

Region: Mumbai (ap-south-1)

Operating System: Amazon Linux 2023

Instance Type: t3.micro

🎯 Learning Objectives

Understand AWS EC2 cloud infrastructure

Learn Linux SSH authentication monitoring

Analyze security logs using Python

Detect suspicious authentication activity

Automate security monitoring

Monitor AWS infrastructure using CloudWatch

Understand CloudWatch alarms and SNS notifications

Build a security dashboard using Streamlit

Practice Git and GitHub version control

👨‍💻 Author

Aman Joshi

GitHub: Amanjoshi-001
