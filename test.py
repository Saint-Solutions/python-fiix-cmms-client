from client.fiix import Client
import os
from dotenv import dotenv_values

config = dotenv_values(".env")

# print(config['API_KEY'])



test = Client(subdomain=config['SUBDOMAIN'], api_key=config['API_KEY'], access_key=config['ACCESS_KEY'], api_secret=config['API_SECRET'])

context = {
    "className": "User",
    "fields": "id, strUserName, strFullName, strUserTitle, intUserStatusID, strPersonnelCode, cf_intSiteIDs"
}


r = test.find(context=context)
print(r)