import requests
from requests import RequestException

api_key = "61be9d5c662f09067ac10595aeeef727"


def get_weather_data(city_name: str, api_key: str) -> float | None:
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = base_url + "?appid=" + api_key + "&q=" + city_name
    try:
        response = requests.get(complete_url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Http Error:", e)
        return None
    except requests.exceptions.ConnectionError as e:
        print("Error Connecting:", e)
        return None
    except requests.exceptions.Timeout as e:
        print("Timeout Error:", e)
        return None
    except requests.exceptions.TooManyRedirects as e:
        print("Too many redirects:", e)
        return None
    except requests.exceptions.RequestException as e:
        print(f"Unknown error: {e}")
        return None

    x = response.json()
    current_temperature = x["main"]["temp"] - 273.15
    return current_temperature


city_name = input("Enter a city name: ")
temperature = get_weather_data(city_name, api_key)

if temperature:
    rounded_temperature = round(temperature, 3)
    print(f"{city_name}'s temperature is: {rounded_temperature}°C")
