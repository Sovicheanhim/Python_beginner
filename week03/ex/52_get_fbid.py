def get_fbid(fb_url):
    import requests
    URL = "https://findmyfbid.com/"

    PARAMS = {'url': fb_url}
    try:
        r = requests.post(url = URL, params= PARAMS)
        return r.status_code, r.json().get("id")
    except Exception:
        return r.status_code, 0

# print(get_fbid("sovichea.nhim"))t