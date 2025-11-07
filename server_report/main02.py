from server_report.report_generator import generate_report
from server_report.email_sender import send_email

def main():
    generate_report()
    send_email()

if __name__ == "__main__":
    main()
