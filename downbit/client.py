import requests as _requests

def get_api(url, params={}, headers={}):
    response = _requests.get(
        url=url,
        params=params,
        headers=headers,
        timeout=1000
    )
    response.raise_for_status()
    return response
