from data_scraper import DataPuller
from data_scraper_config import ScraperConfig
from pprint import pprint

def main():
    pass

    data = ScraperConfig()
    pprint(data.full_url)
    DataPuller.get_data(data.full_url)


if __name__ == "__main__":
    main()