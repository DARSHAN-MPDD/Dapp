import requests

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch exchange rates.")
    data = response.json()
    if "rates" not in data or to_currency.upper() not in data["rates"]:
        raise ValueError("Invalid currency code.")
    return data["rates"][to_currency.upper()]

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    return amount * rate

if __name__ == "__main__":
    try:
        amount = float(input("Enter amount: "))
        from_currency = input("From currency (e.g., USD): ")
        to_currency = input("To currency (e.g., EUR): ")
        result = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
    except Exception as e:
        print("Error:", e)