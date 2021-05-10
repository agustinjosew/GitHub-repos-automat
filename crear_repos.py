import requests
from pprint import pprint


# entry point
if __name__ == "__main__":

    API_URL = "https://api.github.com"
    payload = '{"name":"agustinjosew"}'
    r = requests.post(API_URL+"/user/repos", data=payload)
    pprint(r.json())