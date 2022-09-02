import pandas as pd
import bs4 as bs
import requests
from pprint import pprint


class DataPuller:

    def __init__(self, base_url: str, uri):
        self.base_url = base_url
        self.uri = uri

    def get_data(self):
        res = requests.get(f'{self.base_url}{self.uri}')
        return res.content
