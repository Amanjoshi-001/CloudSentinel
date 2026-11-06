import time
import subprocess

while True:
    print("\nCloudSentinel Automatic SSH Monitor")
    print("----------------------------------")

    result = subprocess.run(
        ["python3", "real_ssh_monitor.py"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    print("Next check in 10 seconds...")
    time.sleep(10)
