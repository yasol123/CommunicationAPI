from email_service_interface import EmailServiceInterface
from email_sender import EmailSender

class EmailService(EmailServiceInterface):
    def __init__(self):
        self.email_sender = EmailSender()

    def send_email(self, to_email: str, subject: str, body: str) -> dict:
        return self.email_sender.send_email(to_email, subject, body)

    def send_welcome_email(self, to_email: str) -> dict:
        subject = 'Welcome to Our Service!'
        body = 'Thank you for signing up. We are excited to have you!'
        return self.send_email(to_email, subject, body)

    def send_billing_email(self, to_email: str) -> dict:
        subject = 'Your Recent Billing Statement'
        body = 'Please find your recent billing statement attached.'
        return self.send_email(to_email, subject, body)

    def send_notification_email(self, to_email: str) -> dict:
        subject = 'Important Notification'
        body = 'You have a new notification. Please check your account for details.'
        return self.send_email(to_email, subject, body)
