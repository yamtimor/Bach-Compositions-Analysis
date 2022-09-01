from pprint import pprint

class ScraperConfig:

    base_url: str = 'https://imslp.org/'
    uri: str = 'wiki/List_of_works_by_Johann_Sebastian_Bach'

    def __call__(self):
        return self.base_url + self.uri

data = ScraperConfig()

pprint(data)