CloudSentinel – AWS Cloud Security Monitoring Project

Project Overview

CloudSentinel is a beginner-friendly AWS cloud security project designed to monitor SSH login activity on an Amazon EC2 instance and detect suspicious login attempts.

Technologies Used

AWS EC2

Amazon Linux 2023

Python 3

Linux SSH

Linux Journal Logs

Project Features

Sample SSH log analysis

Detection of failed SSH password attempts

Severity classification: LOW, MEDIUM, HIGH

Real-time server SSH log monitoring

Automatic monitoring every 10 seconds

Security report generation

Project Files

app.py – Application file

detect_logs.py – Sample SSH log detection

sample_ssh.log – Sample SSH activity logs

detection_report.txt – Sample log analysis report

real_ssh_monitor.py – Real SSH monitoring script

real_ssh_report.txt – Real SSH monitoring report

auto_monitor.py – Automatic SSH monitoring loop

security_report.txt – Security report

How to Run

Analyze Sample Logs

python3 detect_logs.py

Monitor Real SSH Logs

python3 real_ssh_monitor.py

Start Automatic Monitoring

python3 auto_monitor.py

The automatic monitor checks SSH activity every 10 seconds and updates the monitoring report.

Severity Levels

LOW: 0–2 failed SSH password attempts

MEDIUM: 3–4 failed SSH password attempts

HIGH: 5 or more failed SSH password attempts

Learning Objectives

Understand AWS EC2

Learn Linux SSH monitoring

Analyze security logs using Python

Detect suspicious authentication activity

Automate security monitoring

Project Status

Day 6 – Automatic SSH Monitoring Implemented
