import requests
API_KEY= "e7fbaadd192cfbcddb75261f8e16e94c"
BASE_URL="http://api.openweathermap.org/data/2.5/weather"

city=input("enter a city name:")
requests_url= f"{BASE_URL}?appid={API_KEY}&q={city}"
response=requests.get(requests_url)

if response.status_code==200:
 data=response.json()
 weather=data['weather'][0]['description']
 temperature=round(data["main"]["temp"]-273.15)
 print("temperature:",temperature,"celsius")
 print("weather:",weather)
else:
    print("an error ocurred.")








