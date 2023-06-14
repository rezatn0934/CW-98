import requests


def get_data(url: str) -> dict | None:
    try:
        response = requests.get(url, timeout=10)
        return response.json()
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



def process_data(data):
    movies = dict()
    for movie in data:
       movies[movie['Title']] = movie
    return movies


count_process = 0


def count_process_func(input_data):
    def inner_function() -> int:
        global count_process
        nonlocal input_data
        count_process += len(input_data)
        return count_process
    return inner_function()


url = "https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api/movies"

data = get_data(url)
processed_data = process_data(data)
num = count_process_func(processed_data)
print(f"The number of procees is : {num}")
