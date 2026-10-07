import json
from datetime import datetime
from models.analyzer import analyze_alert

log_file = "data/sample.log"

failed_logins = {}
suspicious_logins = []

with open(log_file, "r") as file:
    for line in file:
        parts = line.strip().split()

        timestamp = parts[0] + " " + parts[1]
        username = parts[2]
        ip_address = parts[3]
        action = parts[4]
        result = parts[5]

        if action == "LOGIN" and result == "FAILED":
            failed_logins[ip_address] = failed_logins.get(ip_address, 0) + 1

        elif action == "LOGIN" and result == "SUCCESS":
            previous_failures = failed_logins.get(ip_address, 0)

            if previous_failures >= 3:
                suspicious_logins.append({
                    "type": "SUSPICIOUS_LOGIN",
                    "ip_address": ip_address,
                    "username": username,
                    "previous_failed_attempts": previous_failures,
                    "severity": "MEDIUM"
                })

alerts = []

for ip, count in failed_logins.items():
    if count >= 5:
        alert = {
            "type": "BRUTE_FORCE",
            "ip_address": ip,
            "failed_attempts": count,
            "severity": "HIGH"
        }

        alert["ai_analysis"] = analyze_alert(alert)

        alerts.append(alert)


for alert in suspicious_logins:
    alert["ai_analysis"] = analyze_alert(alert)
    alerts.append(alert)


with open("data/alerts.json", "w") as file:
    json.dump(alerts, file, indent=4)


print("\n===== SECURITY ALERT REPORT =====")
print("Report Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Total Alerts:", len(alerts))

for alert in alerts:
    print("\nAlert Type:", alert["type"])
    print("IP Address:", alert["ip_address"])
    print("Severity:", alert["severity"])

    if "failed_attempts" in alert:
        print("Failed Attempts:", alert["failed_attempts"])

    if "username" in alert:
        print("Username:", alert["username"])

    print("\nAI Analysis:")
    print(alert["ai_analysis"])
    