import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class KeyVaultClient:
    def __init__(self, key_vault_url: str):
        self.client = SecretClient(vault_url=key_vault_url, credential=DefaultAzureCredential())

    def get_secret(self, secret_name: str) -> str:
        secret = self.client.get_secret(secret_name)
        return secret.value
