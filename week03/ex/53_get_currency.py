import requests
from datetime import datetime
def get_currency(currency_list):
    try:
        currency_string = ', '.join([x for x in currency_list])
        URL = "https://www.freeforexapi.com/api/live"
        PARAMS = {'pairs': currency_string}
        r  = requests.post(url= URL, params = PARAMS)
        # print(r.url)
        currency = r.json()
        print(currency)
        currency_rate = currency.get("rates")
        result = list()
        for i in range(len(currency_list)):
            timestamp = datetime.fromtimestamp(currency_rate[currency_list[i]]["timestamp"])
            timestamp = timestamp.strftime("%m/%d/%Y %H:%M")
            temp = (currency_list[i],) + (currency_rate[currency_list[i]]["rate"],) + (currency_rate[currency_list[i]]["timestamp"],) + (timestamp,)
            result += (temp,)
        return result
    except Exception:
        return "The currency pair "+ str(currency_list) +" was not recognised or supported"
# print(get_currency(['EURUSD', 'EURGBP']))
