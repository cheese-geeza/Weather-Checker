import requests

#put API key from https://home.openweathermap.org/
API_KEY = "put api key here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#getting the city name for the API
city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

#error checker
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'])

    print("The weather at " + city + " is", temperature -273, "celsius with", weather)

else :
    print("An error occurred")

