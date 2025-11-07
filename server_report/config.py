import os
import datetime

# Email settings
EMAIL_SETTINGS = {
    "from": "ahojlaxman@gmail.com",
    "to": "lthandalam@outlook.cz",
    "subject": "Html report",
    "smtp_server": "smtp.gmail.com",
    "port": 587,
    "username": "ahojlaxman@gmail.com",
    "password": "pwxm sndc zjzh wpij",  # Use environment variable or secure vault in production
}

# Log paths
TIMESTAMP = datetime.datetime.now().strftime('%Y%m%d-%H%M')
LOG_DIR = "C:\\tools\\logs"
HTML_REPORT = os.path.join(LOG_DIR, f"{TIMESTAMP}_lds_test_report.html")
PDF_REPORT = os.path.join(LOG_DIR, f"{TIMESTAMP}_lds_test_report.pdf")

# Services to check
SERVICES = [
    {"name": "Dhcp", "log": os.path.join(LOG_DIR, "log.txt")},
    {"name": "Dnscache", "log": os.path.join(LOG_DIR, "log.txt")},
    {"name": "PlugPlay", "log": os.path.join(LOG_DIR, "log.txt")},
    {"name": "Spooler", "log": os.path.join(LOG_DIR, "log.txt")},
]
