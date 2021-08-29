


# fiixCmmsClient.setBaseUri(`${process.env.FIIX_URI}/api/`);
# fiixCmmsClient.setAppKey(process.env.APP_KEY);
# fiixCmmsClient.setAuthToken(process.env.API_KEY);
# fiixCmmsClient.setPKey(process.env.API_SECRET);


class FiixClient:
    def __init__(self, fiix_uri, app_key, api_key, api_secret):
        self.fiix_uri = fiix_uri
        self.app_key = app_key
        self.api_key = api_key
        self.api_secret = api_secret