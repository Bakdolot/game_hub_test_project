import requests


def url_check(url: str) -> int:
    response = requests.get(url)
    return response.status_code
