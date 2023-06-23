import requests
import openai
from config import APIKEY_WEATHER,  APIKEY_OpenAI

def get_weather_information(query):

    url = "http://api.weatherstack.com/current"
    
    parameters = {
        "access_key": APIKEY_WEATHER,    
        "query": query
    }

    response = requests.get(url, params = parameters)

    if response.status_code == 200:    
        data = response.json()
        data = response.json()
        temperature = data["current"]["temperature"]
        description = data["current"]["weather_descriptions"][0]

        return (temperature, description)

    else:
        print ("Error")

query = input ("¿En qué ciudad quieres conocer el tiempo? ")   
temp , desc = get_weather_information(query)

# https://platform.openai.com/docs/guides/gpt/chat-completions-api

# Chat Completions API  https://platform.openai.com/docs/guides/gpt/chat-completions-api
openai.api_key = APIKEY_OpenAI

#model https://platform.openai.com/docs/models/overview
print("La temperatura es ", temp)
translation = f"Traduce la siguiente frase a castellano: {desc}"
accion_to_do = f"¿Qué actividad puedo hacer en {query}?"

resp = openai.ChatCompletion.create(model = "gpt-3.5-turbo",
                             messages = [{"role":"user","content": translation},
                                         {"role":"user","content": accion_to_do}])

print(resp.choices[0].message.content)
