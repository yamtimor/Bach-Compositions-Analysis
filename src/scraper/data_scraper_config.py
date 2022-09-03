from pprint import pprint
from pydantic import BaseSettings

class ScraperConfig(BaseSettings):

    base_url: str = 'https://imslp.org/'
    uri: str = 'wiki/List_of_works_by_Johann_Sebastian_Bach'


    def __call__(self):
        print(self.base_url + self.uri)
        return self.base_url + self.uri

data = ScraperConfig()

pprint(data)