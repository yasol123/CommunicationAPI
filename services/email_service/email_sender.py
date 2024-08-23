import smtplib
from email.mime.text import MIMEText
from config.settings import settings

class EmailSender:
    def __init__(self):
        self.smtp_server = 'smtp.example.com'  # Replace with actual SMTP server
        self.smtp_port = 587
        self.smtp_user = settings.get_smtp_user()
        self.smtp_password = settings.get_smtp_password()
        self.sender_email = 'no-reply@example.com'

    def send_email(self, to_email: str, subject: str, body: str) -> dict:
        try:
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = to_email

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)

            return {'status': 'success', 'message': 'Email sent successfully'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
