def get_html():
    import requests
    url = "https://www.google.com"
    # get function is used for packaging the request, send the request and catch the response
    r = requests.get(url)
    return r.text

# from urllib.request import urlopen, Request
#
# url = "https://www.google.com"
#
# request = Request(url)
# response  = urlopen(request)
# html = response.read()
#
#
# response.close()
# print(html)