import os
import smtplib
from email.message import EmailMessage
from server_report.config import EMAIL_SETTINGS, PDF_REPORT
from server_report.logger import logger

def send_email():
    try:
        msg = EmailMessage()
        msg['Subject'] = EMAIL_SETTINGS['subject']
        msg['From'] = EMAIL_SETTINGS['from']
        msg['To'] = EMAIL_SETTINGS['to']
        msg.set_content("Test html report")

        with open(PDF_REPORT, 'rb') as f:
            msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=os.path.basename(PDF_REPORT))

        with smtplib.SMTP(EMAIL_SETTINGS['smtp_server'], EMAIL_SETTINGS['port']) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_SETTINGS['username'], EMAIL_SETTINGS['password'])
            smtp.send_message(msg)

        logger.info("Email sent successfully.")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
