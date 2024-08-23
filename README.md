**CommunicationAPI**

CommunicationAPI is a Flask-based API service designed to handle email communications. 
It supports sending welcome emails, billing emails, and notification emails, and integrates with Salesforce Marketing Cloud for email delivery. 
The project follows SOLID principles and utilizes a structured design pattern for maintainable and scalable code.

**Features**
Send Welcome Email: Automatically sends a welcome email to new users.
Send Billing Email: Sends billing information to users.
Send Notification Email: Delivers various notifications to users.
Salesforce Marketing Cloud Integration: Uses Salesforce Marketing Cloud API for sending emails.
Environment Configuration: Securely manages sensitive data using .env files and Azure KeyVault.

**Project Structure**

```plaintext
CommunicationAPI/
│
├── app.py
├── services/
│   ├── email_service/
│   │   ├── __init__.py
│   │   ├── email_sender.py
│   │   ├── email_service.py
│   │   └── email_service_interface.py
│   └── sfmc_service/
│       ├── __init__.py
│       ├── create_sfmc_client.py
│       └── salesforce_sfmc.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
├── requirements.txt
└── utility/
    └── keyvault.py
  
  app.py: The main entry point of the Flask application.
  services/: Contains business logic for email services and Salesforce Marketing Cloud integration.
  config/: Holds configuration settings, including environment settings and secrets management.
  api_clients/: Contains API client implementations, like the Salesforce Marketing Cloud client.
  utility/: Utilities like Azure KeyVault integration for managing secrets.

**Setup and Installation**
1. Clone the repository:

  git clone https://github.com/yasol123/CommunicationAPI.git
  cd CommunicationAPI

2. Create and activate a virtual environment:
  python3 -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
pip install -r requirements.txt
4. Set up environment variables:
Create a .env file in the project root with the necessary configuration settings. Example:
  FLASK_ENV=development
  SFMC_CLIENT_ID=your_sfmc_client_id
  SFMC_CLIENT_SECRET=your_sfmc_client_secret
  SFMC_AUTH_URL=https://auth.example.com/v2/token
  SFMC_API_URL=https://api.example.com/

**Configuration**
  AWS Database Connection: Configurations for AWS database connections are managed through settings.py and secured using Azure KeyVault.
  Salesforce Marketing Cloud: API credentials and endpoints are configured via environment variables or Azure KeyVault.
**Usage**
1. Run the Flask application:
flask run
The API will be available at http://localhost:5000.
2. API Endpoints:
  Send Welcome Email: POST /api/email/welcome
  Send Billing Email: POST /api/email/billing
  Send Notification Email: POST /api/email/notification
  Each endpoint expects a JSON payload with relevant user information.
**Running Tests**
To run tests, use the following command:
pytest

Ensure you have test cases defined and pytest installed in your environment.

**Contributing**
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch-name).
3. Commit your changes (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-branch-name).
5. Create a new Pull Request.
