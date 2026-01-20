import pytest
from utils.api_helper import APIHelper
from utils.config_reader import ConfigReader

class TestAPI:

    def test_api_get(self):
        self.api = APIHelper(ConfigReader.get_api_base_url())
        response = self.api.api_get("posts/1/comments",params=None)
        assert response[1]["id"] == 2
        assert response[1]["name"] == "quo vero reiciendis velit similique earum"
        assert response[1]["email"] == "Jayne_Kuhic@sydney.com"
