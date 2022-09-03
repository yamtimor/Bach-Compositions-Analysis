import pandas as pd
import bs4 as bs
import requests
from pprint import pprint
from data_scraper_config import ScraperConfig



class DataPuller:

    def __init__(self, full_url):
        self.full_url = full_url

    def get_data(self):
        res = requests.get(self.full_url)
        return res.content
