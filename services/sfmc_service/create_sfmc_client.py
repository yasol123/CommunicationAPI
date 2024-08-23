from config.settings import settings
from salesforce_sfmc import SalesforceSFMCClient

def create_sfmc_client():
    return SalesforceSFMCClient(
        auth_url='https://YOUR_AUTH_ENDPOINT/v2/token',  # Replace with actual auth endpoint
        api_base_url='https://YOUR_API_ENDPOINT',  # Replace with actual SFMC API base URL
        client_id=settings.get_sfmc_client_id(),
        client_secret=settings.get_sfmc_client_secret(),
        resource_id=settings.get_sfmc_resource_id()
    )