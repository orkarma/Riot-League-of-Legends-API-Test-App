
import requests
import RiotConsts as Consts

class RiotAPI(object) :

    def __init__(self, api_key, region=Consts.REGIONS['europe_west']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params=()):
        args = {'api_key' : self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                region=self.region,
                api_url=api_url
                ),
            params=args
            )
        return response.json()
