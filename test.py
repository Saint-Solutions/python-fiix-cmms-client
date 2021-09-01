from client.fiix import Client
import os
from dotenv import dotenv_values

config = dotenv_values(".env")

# print(config['API_KEY'])

client_version = {"clientVersion": {"major": 2, "minor": 8, "patch": 1}}

test = Client(subdomain=config['SUBDOMAIN'], api_key=config['API_KEY'],
              access_key=config['ACCESS_KEY'], api_secret=config['API_SECRET'], version=client_version)

context = {
    "requests": [
		{
			"_maCn" : "FindRequest",
			"className": "Account",
			"fields": "id, strCode, strDescription"
		},{
			"_maCn" : "FindRequest",
			"className": "PurchaseOrder",
			"fields": "id, intCode, intPurchaseOrderStatusID, intSupplierID",
			"filters": [{"ql": "intSupplierID > ? and intSupplierID < ?", "parameters" : [259605, 259610]}]
		}
	  ]
}


r = test.batch(context=context)
print(r.json())
