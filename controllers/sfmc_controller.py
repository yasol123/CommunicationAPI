from flask import Blueprint, request, jsonify
from services.sfmc_service.salesforce_sfmc import SFMCClient
from config.settings import settings
# Create a Blueprint for the Salesforce Marketing Cloud routes
sfmc_controller = Blueprint('sfmc_controller', __name__)

# Initialize the SFMC client using the settings from the configuration
sfmc_client = SFMCClient(
    auth_url=settings.SFMC_AUTH_URL,
    api_base_url=settings.SFMC_API_BASE_URL,
    client_id=settings.SFMC_CLIENT_ID,
    client_secret=settings.SFMC_CLIENT_SECRET,
    resource_id=settings.SFMC_RESOURCE_ID
)

@sfmc_controller.route('/sfmc-data', methods=['GET'])
def get_sfmc_data():
    response = sfmc_client.make_api_request('some/endpoint', 'GET')
    return jsonify(response), 200

@sfmc_controller.route('/send-message', methods=['POST'])
def send_message():
    data = request.json  # Get the JSON payload from the request
    if not data or 'subject' not in data or 'body' not in data or 'recipient' not in data:
        return jsonify({'error': 'Invalid request, subject, body, and recipient are required'}), 400

    sfmc_payload = {
        "From": {
            "Address": "no-reply@yourdomain.com",
            "Name": "Your Service Name"
        },
        "To": {
            "Address": data['recipient'],
            "SubscriberKey": data['recipient'],
            "ContactAttributes": {
                "SubscriberAttributes": {
                    "FirstName": data.get('first_name', ''),
                    "LastName": data.get('last_name', '')
                }
            }
        },
        "Options": {
            "RequestType": "ASYNC"
        },
        "Content": {
            "Subject": data['subject'],
            "HTMLBody": data['body']
        }
    }

    endpoint = 'email/send'  # Example endpoint for sending an email in SFMC
    try:
        response = sfmc_client.make_api_request(endpoint, 'POST', sfmc_payload)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500