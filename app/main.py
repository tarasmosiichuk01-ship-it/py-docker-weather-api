import os

import requests

API_KEY = os.environ.get("API_KEY")

URL = "http://api.weatherapi.com/v1/current.json"

CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        print("Error: API_KEY environment variable is not set")
        return
    response = requests.get(URL, params={"key": API_KEY, "q": CITY})
    if response.status_code != 200:
        print("Error: status code is not 200")
        return
    try:
        data = response.json()
    except ValueError:
        print(f"Error: status code {response.status_code} — {response.text}")
        return
    error = data.get("error")
    if error:
        print(error.get("message", "Unknown API error"))
        return
    print(
        f'{data["location"]["name"]}/{data["location"]["country"]} '
        f'{data["location"]["localtime"]} '
        f'Weather: {data["current"]["temp_c"]} Celsius, '
        f'{data["current"]["condition"]["text"]}'
    )


if __name__ == "__main__":
    get_weather()
