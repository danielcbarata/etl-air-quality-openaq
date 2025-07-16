import requests

SENSOR_ID = 23534
START_DATE = "2024-01-01"
END_DATE = "2024-12-31"

url = f"https://api.openaq.org/v3/sensors/{SENSOR_ID}/days"
params = {
        "date_from": START_DATE,
        "date_to": END_DATE,
        "limit": 1000,  # limite máximo
        "page": 1
    }
headers = {
    "X-API-Key": "a4d5fc3bf09ae68762bd91b7d2c3b974de21940dd37a85286d6618587416a41f"
}

response = requests.get(url, headers=headers)
print("Status code:", response.status_code)
print("Response JSON:", response.json())