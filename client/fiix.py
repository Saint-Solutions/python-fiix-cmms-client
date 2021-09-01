import requests
import hashlib
import hmac
import json

class Client(object):
    def __init__(self, subdomain, api_key, access_key, api_secret):
        self.subdomain = subdomain
        self.api_key = api_key
        self.access_key = access_key
        self.api_secret = api_secret
        self.base_url = 'https://{}.macmms.com/api/?service=cmms&appKey={}&accessKey={}&signatureMethod=HmacSHA256&signatureVersion=1'.format(
            self.subdomain, self.api_key, self.access_key)
        self.msg_url = self.base_url.replace("https://", "")
        self.sig = hmac.new(self.api_secret.encode('utf-8'),
                            self.msg_url.encode('utf-8'), hashlib.sha256).hexdigest()
    # Generate HMAC Authorization String

    def _default_headers(self):
        headers = {
            "Authorization": self.sig,
            "Content-Type": "text/plain"
        }

        return headers

    def __request(self, body):
        r = requests.post(self.base_url, data=body,
                          headers=self._default_headers())

        return r.json()

    def find(self, context):
        find_body = {
            "_maCn": "FindRequest",
            "clientVersion": {"major": 2, "minor": 8, "patch": 1},
            "className": "User",
            "fields": "id, strUserName, strFullName, strUserTitle, intUserStatusID, strPersonnelCode, cf_intSiteIDs"
        }

        return self.__request(json.dumps(find_body))
