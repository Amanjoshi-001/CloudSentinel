import streamlit as st
import subprocess
import sys
import pandas as pd
import boto3
from datetime import datetime, timedelta, timezone

def get_cloudwatch_cpu():
    cloudwatch = boto3.client("cloudwatch", region_name="ap-south-1")

    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(hours=1)

    response = cloudwatch.get_metric_statistics(
        Namespace="AWS/EC2",
        MetricName="CPUUtilization",
        Dimensions=[
            {
                "Name": "InstanceId",
                "Value": "i-045452cdc51cb0be1"
            }
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=["Average"]
    )

    datapoints = sorted(
        response["Datapoints"],
        key=lambda point: point["Timestamp"]
    )

    return pd.DataFrame(datapoints)
    
def get_ec2_health():
    cloudwatch = boto3.client("cloudwatch", region_name="ap-south-1")

    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(hours=1)

    health_metrics = {}

    for metric in ["StatusCheckFailed_Instance", "StatusCheckFailed_System"]:
        response = cloudwatch.get_metric_statistics(
            Namespace="AWS/EC2",
            MetricName=metric,
            Dimensions=[
                {
                    "Name": "InstanceId",
                    "Value": "i-045452cdc51cb0be1"
                }
            ],
            StartTime=start_time,
            EndTime=end_time,
            Period=300,
            Statistics=["Maximum"]
        )

        datapoints = sorted(
            response["Datapoints"],
            key=lambda point: point["Timestamp"]
        )

        health_metrics[metric] = (
            datapoints[-1]["Maximum"] if datapoints else None
        )

    return health_metrics

def get_cloudwatch_alarm():
    cloudwatch = boto3.client("cloudwatch", region_name="ap-south-1")

    response = cloudwatch.describe_alarms(
        AlarmNames=["CloudSentinel-High-CPU-Alarm"]
    )

    alarms = response["MetricAlarms"]

    if alarms:
        return alarms[0]["StateValue"]

    return "NOT_FOUND"

st.set_page_config(
    page_title="CloudSentinel Security Dashboard",
    layout="wide"
)

# SIDEBAR
with st.sidebar:
    st.title("CloudSentinel")
    st.write("AWS Security Monitoring")
    st.divider()
    st.info("Live SSH Login Monitoring")
    st.divider()
    st.subheader("Threat Status")

# DASHBOARD HEADER
st.title("CloudSentinel Security Dashboard")
if st.button("Refresh Dashboard"):
    st.rerun()
st.subheader("Welcome to CloudSentinel")
st.write("AWS Cloud Security Monitoring Project")
st.success("Dashboard is running successfully!")


@st.fragment(run_every="10s")
def security_dashboard():

    # RUN SSH MONITOR AUTOMATICALLY
    try:
        result = subprocess.run(
            [sys.executable, "real_ssh_monitor.py"],
            capture_output=True,
            text=True,
            timeout=20
        )

        if result.returncode != 0:
            st.error("SSH monitoring script encountered an error.")
            st.code(result.stderr)

    except subprocess.TimeoutExpired:
        st.error("SSH monitoring script timed out.")
          
           # CLOUDWATCH CPU MONITORING
    st.subheader("AWS CloudWatch CPU Monitoring")

    try:
        cpu_data = get_cloudwatch_cpu()

        if not cpu_data.empty:
            st.line_chart(
                cpu_data,
                x="Timestamp",
                y="Average"
            )
            st.metric(
                "Latest CPU Usage",
                f"{cpu_data.iloc[-1]['Average']:.2f}%"
            )
        else:
            st.info("No CloudWatch CPU metrics available yet.")

        alarm_state = get_cloudwatch_alarm()
     
        if alarm_state == "OK":
            st.success("🟢 CloudWatch CPU Alarm: OK")

        elif alarm_state == "ALARM":
            st.error("🔴 CloudWatch CPU Alarm: ALARM")

        elif alarm_state == "INSUFFICIENT_DATA":
            st.warning("🟡 CloudWatch CPU Alarm: INSUFFICIENT DATA")

        else:
            st.info(f"CloudWatch CPU Alarm: {alarm_state}")

    except Exception as e:
        st.error(f"CloudWatch monitoring error: {e}")      
       
    # EC2 INSTANCE HEALTH MONITORING
    st.subheader("EC2 Instance Health")

    try:
        health = get_ec2_health()

        col1, col2 = st.columns(2)

        with col1:
            instance_status = health["StatusCheckFailed_Instance"]
            st.metric(
                "Instance Status",
                "Healthy" if instance_status == 0
                else "Failed" if instance_status is not None
                else "No Data"
            )

        with col2:
            system_status = health["StatusCheckFailed_System"]
            st.metric(
                "System Status",
                "Healthy" if system_status == 0
                else "Failed" if system_status is not None
                else "No Data"
            )

    except Exception as e:
        st.error(f"EC2 health monitoring error: {e}")

       # RECENT SSH EVENTS
    st.subheader("Recent SSH Events")
    recent_events = []

    try:
        with open("ssh_login_history.log", "r") as file:
            for line in file:
                if "Accepted publickey" in line:
                    event = "Successful Login"
                elif "Failed password" in line:
                    event = "Failed Login"
                else:
                    continue

                recent_events.append({
                    "Timestamp": " ".join(line.split()[:3]),
                    "Event": event,
                    "Details": line.strip()
                })

        if recent_events:
            df = pd.DataFrame(recent_events[-10:][::-1])

            def color_event(value):
                if value == "Failed Login":
                    return "color: red; font-weight: bold"
                elif value == "Successful Login":
                    return "color: green; font-weight: bold"
                return ""

            styled_df = df.style.applymap(
                color_event,
                subset=["Event"]
            )

            st.dataframe(
                styled_df,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("No SSH login events found.")

    except FileNotFoundError:
        st.warning("SSH history file not found.")

    # READ FRESH REPORT
    report_file = "real_ssh_report.txt"

    successful_logins = 0
    failed_attempts = 0
    threat_level = "UNKNOWN"
    report_timestamp = "Unavailable"

    try:
        with open(report_file, "r") as file:
            for line in file:

                if "Timestamp:" in line:
                    report_timestamp = line.split(":", 1)[1].strip()

                elif "Successful SSH logins:" in line:
                    successful_logins = int(
                        line.split(":", 1)[1].strip()
                    )

                elif "Failed SSH password attempts:" in line:
                    failed_attempts = int(
                        line.split(":", 1)[1].strip()
                    )

                elif "Severity:" in line:
                    threat_level = line.split(":", 1)[1].strip()

    except FileNotFoundError:
        st.error("SSH monitoring report not found.")

    # SECURITY OVERVIEW
    st.header("Security Overview")
    st.caption(f"Last report: {report_timestamp}")

    # CALCULATE SECURITY STATUS
    if threat_level == "HIGH":
        security_status = "CRITICAL"
    elif threat_level == "MEDIUM":
        security_status = "WARNING"
    elif threat_level == "LOW":
        security_status = "SECURE"
    else:
        security_status = "UNKNOWN"

    # Four dashboard metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Failed SSH Logins", failed_attempts)

    with col2:
        st.metric("Successful SSH Logins", successful_logins)

    with col3:
        st.metric("Threat Level", threat_level)

    with col4:
        st.metric("Security Status", security_status)

    # THREAT ANALYSIS - RISK SUMMARY
    st.subheader("Risk Summary")

    # READ ALERT FROM MONITORING REPORT
    try:
        with open("real_ssh_report.txt", "r") as file:
            report_text = file.read()

        alert_line = [
            line for line in report_text.splitlines()
            if line.startswith("Alert:")
        ]

        if alert_line:
            alert_message = alert_line[0].replace(
                "Alert:", ""
            ).strip()

            if alert_message.startswith("CRITICAL"):
                st.error(alert_message)
            elif alert_message.startswith("WARNING"):
                st.warning(alert_message)
            else:
                st.success(alert_message)
        else:
            st.info("No alert information available.")

    except FileNotFoundError:
        st.warning("Security report not found.")


    # LIVE IP ACTIVITY
    st.subheader("Live IP Activity")

    try:
        subprocess.run(
            [sys.executable, "live_ip_detector.py"],
            capture_output=True,
            text=True,
            timeout=30
        )

        with open("live_ip_report.txt", "r") as file:
            live_report = file.read()

        st.text(live_report)

    except Exception as e:
        st.warning(f"Live IP monitoring error: {e}")

    # DISPLAY RISK LEVEL
    if threat_level == "HIGH":
        st.error("HIGH RISK: Critical suspicious SSH activity detected!")
    elif threat_level == "MEDIUM":
        st.warning("MEDIUM RISK: Suspicious SSH activity detected!")
    elif threat_level == "LOW":
        pass
    else:
        st.info("Threat level is currently unknown.")

    # SYSTEM SECURITY STATUS
    st.header("System Security Status")

    if threat_level == "HIGH":
        st.error("Security Status: ATTENTION REQUIRED")
    elif threat_level == "MEDIUM":
        st.warning("Security Status: MONITORING REQUIRED")
    elif threat_level == "LOW":
        st.success("Security Status: SECURE")
    else:
        st.info("Security Status: UNKNOWN")

    # SIDEBAR THREAT INDICATOR
 

    # SSH ACTIVITY CHART
    st.header("SSH Login Activity")

    activity_data = {
        "Login Type": [
            "Failed SSH Logins",
            "Successful SSH Logins"
        ],
        "Count": [
            failed_attempts,
            successful_logins
        ]
    }

    st.bar_chart(
        activity_data,
        x="Count",
        y="Login Type",
        horizontal=True
    )



 # SSH HISTORY SUMMARY
st.header("SSH History Summary")

history_file = "ssh_login_history.log"

history_success = 0
history_failed = 0

try:
    with open(history_file, "r") as file:
        for line in file:
            if "Accepted publickey" in line:
                history_success += 1
            elif "Failed password" in line:
                history_failed += 1

    col1, col2 = st.columns(2)

    with col1:
        st.metric("History Successful Logins", history_success)

    with col2:
        st.metric("History Failed Logins", history_failed)

except FileNotFoundError:
    st.warning("SSH history file not found.")
security_dashboard()
