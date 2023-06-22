import os
import smtplib
from email.message import EmailMessage

SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_EMAIL = os.environ.get("SMTP_EMAIL")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")


class NotificationManager:
    @staticmethod
    def send_emails(self, to_emails, message):
        msg = EmailMessage()
        msg.set_content(message)
        msg["Subject"] = "Low Price Alert"
        msg["From"] = SMTP_EMAIL
        msg["To"] = ", ".join(to_emails)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.send_message(msg)
