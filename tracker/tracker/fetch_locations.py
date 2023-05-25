import urllib,json
import requests
def get_location(ip):
    url=f'https://api.ipfind.com/?ip={ip}'
    r=requests.get(url=url)
    data=json.loads(r.text)
    return data

