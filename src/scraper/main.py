from data_scraper import DataPuller
from data_scraper_config import ScraperConfig
from pprint import pprint

def main():

    data = ScraperConfig()
    # pprint(data.full_url)
    Scraper = DataPuller(data.full_url)
    pprint(Scraper.get_data())


if __name__ == "__main__":
    main()
