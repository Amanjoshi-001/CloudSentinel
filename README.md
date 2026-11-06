# 🛡️ CloudSentinel — AWS Cloud Security Monitoring

## 📌 Project Overview

CloudSentinel is a beginner-friendly AWS cloud security monitoring project built using Python and Amazon EC2.

The project monitors SSH authentication activity on a Linux server, detects failed login attempts, classifies security events based on severity, and generates security reports.

This project demonstrates practical cloud security concepts, Linux log monitoring, Python automation, and GitHub version control.

## 🛠️ Technologies Used

- **AWS EC2** — Cloud server hosting
- **Amazon Linux 2023** — Operating system
- **Python 3** — Security monitoring and log analysis
- **Linux SSH** — Secure remote server access
- **Linux Journal Logs** — SSH authentication event collection
- **Git & GitHub** — Version control and project hosting

## 🚀 Project Features

- Analyze sample SSH authentication logs using Python
- Detect failed SSH password attempts
- Classify security severity as LOW, MEDIUM, or HIGH
- Monitor real SSH authentication events from Linux journal logs
- Automatically execute SSH monitoring every 10 seconds
- Generate security monitoring reports
- Track project changes using Git and GitHub

## 📂 Project Structure

```text
CloudSentinel/
├── app.py
├── detect_logs.py
├── sample_ssh.log
├── detection_report.txt
├── real_ssh_monitor.py
├── real_ssh_report.txt
├── auto_monitor.py
├── security_report.txt
├── README.md
└── .gitignore
```

## ⚙️ How to Run

### 1. Analyze Sample SSH Logs

```bash
python3 detect_logs.py
```

### 2. Monitor Real SSH Activity

```bash
python3 real_ssh_monitor.py
```

### 3. Start Automatic Monitoring

```bash
python3 auto_monitor.py
```

The automatic monitor executes the real SSH monitoring script every 10 seconds.

Press `Ctrl + C` to stop the automatic monitoring loop.

## 🚨 Severity Classification

| Severity | Failed SSH Password Attempts |
|---|---|
| LOW | 0–2 |
| MEDIUM | 3–4 |
| HIGH | 5 or more |

## ☁️ AWS Environment

- **Cloud Provider:** Amazon Web Services
- **Service:** Amazon EC2
- **Region:** Mumbai (ap-south-1)
- **Operating System:** Amazon Linux 2023
- **Instance Type:** t3.micro

## 🎯 Learning Objectives

- Understand AWS EC2 cloud infrastructure
- Learn Linux SSH authentication monitoring
- Analyze security logs using Python
- Detect suspicious authentication activity
- Automate security monitoring
- Practice Git and GitHub version control


## 👨‍💻 Author

Aman Joshi

GitHub: [Amanjoshi-001](https://github.com/Amanjoshi-001)
