import os
import subprocess
from server_report.config import LOG_DIR, HTML_REPORT, PDF_REPORT
from server_report.health_check import perform_health_check
from server_report.service_check import perform_service_check
from server_report.config import SERVICES
from server_report.logger import logger

def generate_report():
    try:
        os.makedirs(LOG_DIR, exist_ok=True)
        open(HTML_REPORT, 'w').close()
        perform_health_check(HTML_REPORT)
        perform_service_check(HTML_REPORT, SERVICES)

        subprocess.run([
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            "--headless", f"--print-to-pdf={PDF_REPORT}", HTML_REPORT
        ], check=False)
        logger.info("Report generated succesfully")
    except Exception as e:
        logger.error(f"Failed to create a report: {e}")

