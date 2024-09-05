import requests

url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

querystring = {"lon":"20.0192","lat":"38.7525","units":"imperial","lang":"en"}

headers = {
 	"x-rapidapi-key": "3d9c3c7db5msh063f33267a155e9p116340jsn6f42ca8e8b40",
 	"x-rapidapi-host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
json_data = response.json()


city_name = json_data['data'][0]['city_name']
country_name = json_data['data'][0]['country_code']
temperature = json_data['data'][0]['temp']


print(f"The weather in {city_name}, {country_name} is {temperature} Fahrenheit right now.")  

