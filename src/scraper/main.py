from data_scraper import DataPuller
from data_scraper_config import ScraperConfig

def main():

    data = ScraperConfig()

    DataPuller.get_data(data())



if __name__ == "__main__":
    main()