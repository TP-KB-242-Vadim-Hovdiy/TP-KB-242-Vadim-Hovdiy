import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

data = response.json()

rates = {}
for elem in data:
    if elem["cc"] in ["EUR", "USD", "PLN"]:
        rates[elem["cc"]] = elem["rate"]

print("Курси валют НБУ (грн за 1 одиницю):")
for currency, rate in rates.items():
    print(f"{currency}: {rate} грн")

currency = input("Введіть валюту (EUR, USD, PLN): ").upper()
amount = float(input("Введіть кількість: "))

if currency in rates:
    result = amount * rates[currency]
    print(f"{amount} {currency} = {result:.2f} UAH")
else:
    print("Невідома валюта. Спробуйте ще раз.")