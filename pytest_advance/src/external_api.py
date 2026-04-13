import requests

class ExternalAPIError(Exception):
    pass

def fetch_user(user_id: int, base_url:str, time_out:int = 5) ->dict:
    url =f"{base_url.rstrip}('/')/users/{user_id}"
    resp = requests.get(url, time_out)
    if resp.status_code !=200:
        raise ExternalAPIError("HTTP 500")
    
    data = resp.json()
    if "id" not in data or "name" not in data:
        raise ExternalAPIError("Invalid schema")
    return data

