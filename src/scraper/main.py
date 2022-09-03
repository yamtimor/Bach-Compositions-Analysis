from data_scraper import DataPuller
from data_scraper_config import ScraperConfig
from pprint import pprint

def main():
    pass

    data = ScraperConfig()
    pprint(DataPuller.get_data(data()))



if __name__ == "__main__":
    main()