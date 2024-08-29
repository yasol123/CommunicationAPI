from config.settings import settings
from .salesforce_sfmc import SFMCClient

def create_sfmc_client():
    return SFMCClient(
        auth_url=settings.SFMC_AUTH_URL,  # Using settings directly
        api_base_url=settings.SFMC_API_BASE_URL,  # Using settings directly
        client_id=settings.SFMC_CLIENT_ID,  # Using settings directly
        client_secret=settings.SFMC_CLIENT_SECRET,  # Using settings directly
        resource_id=settings.SFMC_RESOURCE_ID  # Using settings directly
    )
