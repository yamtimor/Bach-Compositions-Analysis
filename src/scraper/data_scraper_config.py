from pprint import pprint
from pydantic import BaseSettings

class ScraperConfig(BaseSettings):

    base_url: str = 'https://imslp.org/'
    uri: str = 'wiki/List_of_works_by_Johann_Sebastian_Bach'
    full_url: str = base_url+uri

    def __call__(self):
        pass


data = ScraperConfig()

# pprint(data.full_url)