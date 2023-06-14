import requests

url = "https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api/movies"

response = requests.get(url)

if response.status_code == 200:
    movies = response.json()
    # print(movies)
    # with open("data.json", "w") as f:
    #     json.dump(movies, f, indent=4)

    for movie in movies:
        print(f"title: {movie['Title']}, year: {movie['Year']}, runtime: {movie['Runtime']}")
else:
    print("Error:", response.status_code)


title = input("Enter the title of the movie: ")
year = input("Enter the year of the movie: ")
runtime = input("Enter the runtime of the movie: ")

new_movie = {"Title": title, "Year": year, "Runtime": runtime}
print(new_movie)
response = requests.post(url, json=new_movie)

if response.status_code == 201:
    print("Movie added!")
else:
    print("Error adding movie:", response.status_code)
