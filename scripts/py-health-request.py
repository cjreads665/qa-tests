import requests
import time
import logging

logging.basicConfig(level=logging.INFO)

APP_URL = 'https://www.google.com/'

def check_app_status():
    try:
        response = requests.get(APP_URL)
        if response.status_code == 200:
            logging.info("app is up")
        else:
            logging.warning(f"app is down. status code : {response.status_code} ")

    except requests.exceptions.RequestException as err:
        logging.error(f"unable to fetch url. Error : {err}")


if __name__ == "__main__":
    while True:
        check_app_status()
        time.sleep(60)