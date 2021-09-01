from fiixclient import FiixClient
import os
from dotenv import dotenv_values

config = dotenv_values(".env")

client_version = {"clientVersion": {"major": 2, "minor": 8, "patch": 1}}

fiix = FiixClient(subdomain=config['SUBDOMAIN'], api_key=config['API_KEY'],
                  access_key=config['ACCESS_KEY'], api_secret=config['API_SECRET'], version=client_version)

# context = {
#     "requests": [
# 		{
# 			"_maCn" : "FindRequest",
# 			"className": "Account",
# 			"fields": "id, strCode, strDescription"
# 		},{
# 			"_maCn" : "FindRequest",
# 			"className": "PurchaseOrder",
# 			"fields": "id, intCode, intPurchaseOrderStatusID, intSupplierID",
# 			"filters": [{"ql": "intSupplierID > ? and intSupplierID < ?", "parameters" : [259605, 259610]}]
# 		}
# 	  ]
# }

context = {

    "className": "Account",
    "fields": "id, strCode, strDescription"
}

r = fiix.retrieve(context)
print(r.json())
