import streamlit as st
import subprocess
import sys

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

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Failed SSH Logins", failed_attempts)

    with col2:
        st.metric("Successful SSH Logins", successful_logins)

    # THREAT ANALYSIS
    st.header("Threat Analysis")

    if threat_level == "HIGH":
        st.error(f"Threat Severity: {threat_level}")
    elif threat_level == "MEDIUM":
        st.warning(f"Threat Severity: {threat_level}")
    elif threat_level == "LOW":
        st.success(f"Threat Severity: {threat_level}")
    else:
        st.info(f"Threat Severity: {threat_level}")

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
        x="Login Type",
        y="Count"
    )


security_dashboard()
