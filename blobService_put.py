import os
import traceback
from azure.common.credentials import ServicePrincipalCredentials
from msrestazure.azure_exceptions import CloudError
from msrestazure.azure_configuration import AzureConfiguration
from msrest.service_client import ServiceClient
from msrest.polling import LROPoller
from msrestazure.polling.arm_polling import ARMPolling
from msrest.pipeline import ClientRawResponse
import uuid
from dotenv import load_dotenv

project_folder = os.path.expanduser("/home/admin1/Desktop/Jayna/ResourceCreation/venv") # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

SUBSCRIPTION_ID = os.environ.get('AZURE_SUBSCRIPTION_ID')
RESOURCE_GROUP = "AzureResourceGroupJB"
STORAGE_ACCOUNT_NAME = "azurestorageaccountjb"
BLOB_SERVICE_NAME = "azurestorageaccountjb"

BODY = {
  "properties": {
    "cors": {
      "corsRules": [
        {
          "allowedOrigins": [
            "http://www.contoso.com",
            "http://www.fabrikam.com"
          ],
          "allowedMethods": [
            "GET",
            "HEAD",
            "POST",
            "OPTIONS",
            "MERGE",
            "PUT"
          ],
          "maxAgeInSeconds": "100",
          "exposedHeaders": [
            "x-ms-meta-*"
          ],
          "allowedHeaders": [
            "x-ms-meta-abc",
            "x-ms-meta-data*",
            "x-ms-meta-target*"
          ]
        },
        {
          "allowedOrigins": [
            "*"
          ],
          "allowedMethods": [
            "GET"
          ],
          "maxAgeInSeconds": "2",
          "exposedHeaders": [
            "*"
          ],
          "allowedHeaders": [
            "*"
          ]
        },
        {
          "allowedOrigins": [
            "http://www.abc23.com",
            "https://www.fabrikam.com/*"
          ],
          "allowedMethods": [
            "GET",
            "PUT"
          ],
          "maxAgeInSeconds": "2000",
          "exposedHeaders": [
            "x-ms-meta-abc",
            "x-ms-meta-data*",
            "x -ms-meta-target*"
          ],
          "allowedHeaders": [
            "x-ms-meta-12345675754564*"
          ]
        }
      ]
    },
    "defaultServiceVersion": "2017-07-29",
    "deleteRetentionPolicy": {
      "enabled": True,
      "days": "300"
    }
  }
}

API_VERSION = '2018-07-01'

def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id=os.environ.get('AZURE_CLIENT_ID'),
        secret=os.environ.get('AZURE_CLIENT_SECRET'),
        tenant=os.environ.get('AZURE_TENANT_ID')
    )
    return credentials



def run_example():
    credentials = get_credentials()

    config = AzureConfiguration('https://management.azure.com')
    service_client = ServiceClient(credentials, config)

    query_parameters = {}
    query_parameters['api-version'] = API_VERSION

    header_parameters = {}
    header_parameters['Content-Type'] = 'application/json; charset=utf-8'
    #header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())

    operation_config = {}
    request = service_client.put("/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "/blobServices/" + BLOB_SERVICE_NAME, query_parameters)
    response = service_client.send(request, header_parameters, BODY, **operation_config)
    print(response.text)


if __name__ == "__main__":
    run_example()
