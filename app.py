from flask import Flask, render_template, request
from curreny import convert_currency

app = Flask(__name__)

# List of common currency codes (add/remove as needed)
CURRENCIES = [
    "USD", "EUR", "GBP", "INR", "AUD", "CAD", "SGD", "CHF", "MYR", "JPY",
    "CNY", "NZD", "ZAR", "RUB", "BRL", "HKD", "KRW", "SEK", "NOK", "MXN"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_currency = request.form['from_currency']
            to_currency = request.form['to_currency']
            result = convert_currency(amount, from_currency, to_currency)
        except Exception as e:
            error = str(e)
    return render_template('index.html', result=result, error=error, currencies=CURRENCIES)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')