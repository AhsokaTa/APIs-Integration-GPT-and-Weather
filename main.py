import requests
from config import APIKEY

def get_weather_information(query):

    url = "http://api.weatherstack.com/current"

    # access_key = APIKEY    
    #query="Barcelona"
    # request parameters
    
    parameters = {
        "access_key": APIKEY,    
        "query": query
    }

    # GET request to the API
    response = requests.get(url, params = parameters)

    if response.status_code == 200:    
        data = response.json()
        data = response.json()
        temperature = data["current"]["temperature"]
        description = data["current"]["weather_descriptions"][0]
        #return temperature, description

        print(f"Temperatura en {query}: {temperature} º C")
        print(f"Descripción del clima: {description}")
    else:
        print ("Error")
        #return None, None

query = input ("¿En qué ciudad quieres conocer el tiempo? ")   
get_weather_information(query)
