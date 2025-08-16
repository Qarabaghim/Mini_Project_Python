import requests as re
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=3*60*60)


@cached(cache)
def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = re.get(url)
    if response.status_code != 200:
        return None
    return response.json()['rates'][target_currency]


def convert_currency(amount, exchange_rate):
    return amount * exchange_rate


if __name__ == "__main__":
    base_currency = input("Enter the base currency code: ")
    target_currency = input("Enter the target currency code: ")
    amount = float(input("Enter the amount to convert: "))
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = convert_currency(amount, exchange_rate)
    # print(f"The converted amount is {converted_amount}")
    print(f"{amount} {base_currency} is {converted_amount} {target_currency}")
