import requests

API_KEY = "4e57fc58c00641f1a8b155647253010 "  # you’ll get it free from weatherapi.com
city = "Kolkata"

url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

response = requests.get(url)
data = response.json()

print("City:", data["location"]["name"])
print("Temperature:", data["current"]["temp_c"], "°C")
print("Condition:", data["current"]["condition"]["text"])
