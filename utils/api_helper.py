import requests
from typing import Any, Dict, Optional, Union

class APIHelper:

    def __init__(self, api_base_url):
        self.api_base_url = api_base_url
        self.session = requests.Session()
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (pytest-api-tester)'
        }
        self.session.headers.update(self.headers)

    def api_get(self,endpoint,params=None):
        url=f"{self.api_base_url}/{endpoint}" 
        resp = self.session.get(url,params=params)
        resp.raise_for_status()
        return resp.json()

    def api_post(self,endpoint,data=None):
        url=f"{self.api_base_url}/{endpoint}" 
        resp = self.session.post(url,json=data)
        resp.raise_for_status()
        return resp.json()