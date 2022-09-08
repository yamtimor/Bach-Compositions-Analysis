from pprint import pprint
from pydantic import BaseSettings

class API_Config(BaseSettings):

    base_url: str = 'https://imslp.org/'
    uri: str = ""
    full_url: str = base_url+uri

    def __call__(self):
        pass
