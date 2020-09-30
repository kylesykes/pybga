import requests
from . import Game

class BGA:
    def __init__(self, client_id: str, client_secret: str=None, redirect_uri:str =None):
        self._base_url = "https://api.boardgameatlas.com/api/"
        self._client_id = client_id
        self._client_secret = client_secret
        self._redirect_uri = redirect_uri
        self._params = {
            "client_id": self._client_id
        }
        
    def get_list(self, username: str):
        request_url = self._base_url + "lists"
        params = {
            "client_id": self._client_id,
            "username": username
        }
        r = requests.get(request_url, params=params)
        return r.json()

    def get_price(self, game_id: str, pretty: bool = False):
        request_url = self._base_url + "game/prices"
        params = self._params
        params["game_id"] = game_id
        r = requests.get(request_url, params=params)
        return r.json()

