import requests
import hashlib
import hmac
import json


class FiixClient(object):
    def __init__(self, subdomain, api_key, access_key, api_secret, version):
        self.version = version
        self.subdomain = subdomain
        self.api_key = api_key
        self.access_key = access_key
        self.api_secret = api_secret
        self.base_url = 'https://{}.macmms.com/api/?service=cmms&appKey={}&accessKey={}&signatureMethod=HmacSHA256&signatureVersion=1'.format(
            self.subdomain, self.api_key, self.access_key)
        self.msg_url = self.base_url.replace("https://", "")
        self.sig = hmac.new(self.api_secret.encode('utf-8'),
                            self.msg_url.encode('utf-8'), hashlib.sha256).hexdigest()

    def _default_headers(self):
        headers = {
            "Authorization": self.sig,
            "Content-Type": "text/plain;charset=utf-8"
        }

        return headers

    def __request(self, body):
        r = requests.post(self.base_url, data=body,
                          headers=self._default_headers())

        return r

    def create(self, context):
        req_type = '{"_maCn": "AddRequest"}'
        ld = json.loads(req_type)
        ld.update(self.version)
        ld.update(context)

        return self.__request(json.dumps(ld))


    def retrieve(self, context):
        req_type = '{"_maCn": "FindRequest"}'
        ld = json.loads(req_type)
        ld.update(self.version)
        ld.update(context)

        return self.__request(json.dumps(ld))

    def update(self, context):
        req_type = '{"_maCn": "ChangeRequest"}'
        ld = json.loads(req_type)
        ld.update(self.version)
        ld.update(context)

        return self.__request(json.dumps(ld))


    def delete(self, context):
        req_type = '{"_maCn": "RemoveRequest"}'
        ld = json.loads(req_type)
        ld.update(self.version)
        ld.update(context)

        return self.__request(json.dumps(ld))

    def batch(self, context):
        req_type = '{"_maCn": "BatchRequest"}'
        ld = json.loads(req_type)
        ld.update(self.version)
        ld.update(context)

        return self.__request(json.dumps(ld))
