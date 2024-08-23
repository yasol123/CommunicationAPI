from utility.keyvault import KeyVaultClient

class Settings:
    def __init__(self):
        self.key_vault_url = 'https://MyKeyVault.vault.azure.net'
        self.key_vault_client = KeyVaultClient(self.key_vault_url)
        
        # Fetch secrets
        self.smtp_user = self.key_vault_client.get_secret('SMTPUser')
        self.smtp_password = self.key_vault_client.get_secret('SMTPPassword')
        self.sfmc_client_id = self.key_vault_client.get_secret('SFMCClientID')
        self.sfmc_client_secret = self.key_vault_client.get_secret('SFMCClientSecret')
        self.sfmc_resource_id = self.key_vault_client.get_secret('SFMCResourceID')

        self.sfmc_auth_url = 'https://YOUR_AUTH_ENDPOINT/v2/token'  # Replace with actual auth endpoint
        self.sfmc_api_base_url = 'https://YOUR_API_ENDPOINT'  # Replace with actual SFMC API base URL

    def get_smtp_user(self):
        return self.smtp_user

    def get_smtp_password(self):
        return self.smtp_password

    def get_sfmc_client_id(self):
        return self.sfmc_client_id

    def get_sfmc_client_secret(self):
        return self.sfmc_client_secret

    def get_sfmc_resource_id(self):
        return self.sfmc_resource_id

    def get_sfmc_auth_url(self):
        return self.sfmc_auth_url

    def get_sfmc_api_base_url(self):
        return self.sfmc_api_base_url

settings = Settings()
