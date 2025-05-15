import requests
import logging
from logging import log

#TODO: resumable downloads
def retrieve_indicator_data(indicator_code):
    try:
        url = f"https://ghoapi.azureedge.net/api/{indicator_code}"
        response = requests.get(url)
        return response.json()["value"]
    except Exception as e:
        log(logging.ERROR, f"Failed to invoke WHO GHO API {e}")