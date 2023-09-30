import requests    #allows you to send request 

API_KEY = '34ef1f49aac365feb0ec02ff52ebc5ef'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


city = input('\nEnter a city name: ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    temp_convert = round((temperature - 273.15) * 9/5 + 32)
    
    print('Weather:', weather)
    print('temperature:', temp_convert, 'degrees fahrenheit\n')

else:
    print('An error occurred')
    
    
    

