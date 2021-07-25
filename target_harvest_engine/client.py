import backoff
import requests

from logging import getLogger
from typing import Dict


class HarvestEngineAPI:

    def __init__(self, config: Dict) -> None:
        self.logger = getLogger('HarvestEngineAPI')
        self._api_endpoint = str(config["api_url"])
        self._session = requests.Session()
        self._headers = {
            "Accept": "application/json",
            "Content-type": "application/json"
        }

    @backoff.on_exception(
        backoff.expo,
        requests.exceptions.RequestException,
        max_tries=10
    )
    def post(self, payload: Dict) -> None:
        self._session.request(
            'POST',
            f'{self._api_endpoint}',
            json=payload,
            headers=self._headers
        )
