# Fiix CMMS client for JavaScript

The unofficial [Fiix CMMS](https://www.fiixsoftware.com) client for Python.

## Installation

```sh
pip install fiixclient
```

## Setup

Get API keys from your Fiix web application. Not sure how? [Read here](https://fiixlabs.github.io/api-documentation/guide.html#api_keys).

Once you've obtained your API Aplication Key, Access Key and API Secret you're ready to get started. Keep them nearby as we'll use them next.


## Basic Usage and Getting Started

```python
from fiixclient import FiixClient

# Add the client version as required.
client_version = {"clientVersion": {"major": 2, "minor": 8, "patch": 1}}

# Hook up your API Keys. You could also export these to your environment variables.
SUBDOMAIN = "" # eg mycmmstenant (do not include the whole URL)
API_KEY = "" # also known as Application Key
ACCESS_KEY = ""
API_SECRET = ""


# Setup the Fiix Client
fiix = FiixClient(subdomain=SUBDOMAIN, api_key=API_KEY,
              access_key=ACCESS_KEY, api_secret=API_SECRET, version=client_version)
              

# Add context to your requests. For more info check out the CRUD examples https://fiixlabs.github.io/api-documentation/guide-nosdk.html#crud_example
context = {
    "className": "Account",
    "fields": "id, strCode, strDescription"
}

# Methods available are create(), retrieve(), update(), delete() and batch().
r = fiix.retrieve(context)
print(r.json())
# This will return a response in Json

# Batch example

batch_context = {
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

obj = fiix.batch(batch_context)
print(obj)

# Objects returned are based on the Requests library. By default it will return a status code (eg 200).. append .json() to get the json data from the body.


```

Refer to the [documentation](https://fiixlabs.github.io/api-documentation/guide-nosdk.html#crud_example) for more information, especially the request context.


## License

see LICENSE for more information.