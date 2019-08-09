import requests
import base64

DOMAIN = 'eastus2.azuredatabricks.net'
TOKEN = b'dapi08bbae55a78f8864cc7842a610065c1e'

response = requests.post('https://%s/api/2.0/clusters/create' % (DOMAIN),
headers={'Authorization': b"Basic " + base64.standard_b64encode(b"token:" + TOKEN)},
json={
    "num_workers":1,
    "cluster_name": "AzureDatabricksCluster",
    "spark_version": "5.3.x-scala2.11",
    "spark_conf": {},
    "node_type_id": "Standard_DS3_v2",
    "ssh_public_keys": [],
    "custom_tags": {},
    "spark_env_vars": {
    "PYSPARK_PYTHON": "/databricks/python3/bin/python3",
}
}
)
if response.status_code == 200:
    print(response.json()['cluster_id'])
else:
    print("Error launching cluster: %s: %s" % (response.json()["error_code"], response.json()["message"]))