from flask import Blueprint, request, jsonify
from services.email_service.email_service import EmailService

email_controller = Blueprint('email_controller', __name__)
email_service = EmailService()

@email_controller.route('/send/welcome', methods=['POST'])
def send_welcome_email():
    data = request.json
    email = data.get('email')
    if not email:
        return jsonify({'error': 'Email address is required'}), 400
    result = email_service.send_welcome_email(email)
    return jsonify(result), 200

@email_controller.route('/send/billing', methods=['POST'])
def send_billing_email():
    data = request.json
    email = data.get('email')
    if not email:
        return jsonify({'error': 'Email address is required'}), 400
    result = email_service.send_billing_email(email)
    return jsonify(result), 200

@email_controller.route('/send/notification', methods=['POST'])
def send_notification_email():
    data = request.json
    email = data.get('email')
    if not email:
        return jsonify({'error': 'Email address is required'}), 400
    result = email_service.send_notification_email(email)
    return jsonify(result), 200
