# services/sfmc_service/__init__.py

from .salesforce_sfmc import SFMCClient

def create_sfmc_client():
    return SFMCClient(
        auth_url=settings.get_sfmc_auth_url(),
        api_base_url=settings.get_sfmc_api_base_url(),
        client_id=settings.get_sfmc_client_id(),
        client_secret=settings.get_sfmc_client_secret(),
        resource_id=settings.get_sfmc_resource_id()
    )
