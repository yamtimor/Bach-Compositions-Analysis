class ScraperConfig:

    base_url: str = 'https://imslp.org/'
    uri: str = 'wiki/List_of_works_by_Johann_Sebastian_Bach'

    @property
    def full_url(self):
        return self.base_url + self.uri