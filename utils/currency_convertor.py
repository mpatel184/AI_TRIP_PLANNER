import requests

class CurrencyConverter:
    def __init__(self, api_key: str):
        self.base_url = f"https://v6.exchange_rate-api.com/v6/{api_key}/latest/"
        def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
            """
            Convert currency from one type to another.
            Args:
                amount (float): The amount to convert.
                from_currency (str): The currency to convert from.
                to_currency (str): The currency to convert to.
            Returns:
                float: The converted amount.
            """
            url = f"{self.base_url}{from_currency}"
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception(f"Error fetching exchange rates: {response.status_code} - {response.text}")
            data = response.json()
            if 'conversion_rates' in data and to_currency in data['conversion_rates']:
                exchange_rate = data['conversion_rates'][to_currency]
                return amount * exchange_rate
            else:
                raise ValueError(f"Conversion rate not found for {to_currency}")