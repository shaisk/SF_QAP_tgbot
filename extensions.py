import requests
import json


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        try:
            amount = float(amount)
        except ValueError:
            raise APIException("Invalid amount format")

        if base == quote:
            raise APIException(f"Cannot convert the same currency {base}")

        # API URL
        url = f"https://api.exchangerate-api.com/v4/latest/{base.upper()}"
        response = requests.get(url)

        if response.status_code != 200:
            raise APIException("Error fetching data from API")

        data = json.loads(response.text)
        rates = data.get("rates")

        if quote.upper() not in rates:
            raise APIException(f"Currency {quote} not found")

        conversion_rate = rates[quote.upper()]
        total_amount = conversion_rate * amount

        return total_amount
