from collections import Counter

log_file = "ssh_login_history.log"

successful_logins = 0
failed_logins = 0

with open(log_file, "r") as file:
    for line in file:
        if "Accepted publickey" in line:
            successful_logins += 1

        elif "Failed password" in line:
            failed_logins += 1

print("CloudSentinel SSH History Analysis")
print("----------------------------------")
print("Successful SSH Logins:", successful_logins)
print("Failed SSH Logins:", failed_logins)

if failed_logins >= 5:
    print("Threat Level: HIGH")
elif failed_logins >= 3:
    print("Threat Level: MEDIUM")
else:
    print("Threat Level: LOW")
