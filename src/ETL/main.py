from data_puller import DataPuller
from api_config import API_Config
from pprint import pprint

def main():

    # requests
    data = API_Config()
    # pprint(data.full_url)
    datap = DataPuller(data.full_url)
    pprint(datap.get_data())


if __name__ == "__main__":
    main()

