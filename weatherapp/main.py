import requests
import json
import pyttsx3

engine = pyttsx3.init()

while(True):
           x=input("Enter 0 to stop else contionue")
           if(x=="0"):
               break

           engine.say("Welcome to tejas' Weather app")
           engine.say("Enter the name of city to get weather information and alert if rain is there")
           city = input("Enter the name of the city: ")
           url = f"http://api.weatherapi.com/v1/current.json?key=97b89678549e4d64948125409230607&q={city}"
           response = requests.get(url)
           # Convert the JSON response to a dictionary
           data = json.loads(response.text)

           print("Weather Data for", city)


           # Print all parameters from "current" section
           c = data["current"]["condition"]
           sgr=f"Showing weather report on {city}"
           engine.say(sgr)

           print(c["text"])
           if (c["text"] == "Moderate rain"):
               engine.say("Moderate rain is present drive slowly...")
           elif (c["text"] == "Heavy rain"):
               engine.say("Stay at home Heavy rain present")
           else:
               s = f"Rain status:c[text]"
               engine.say(s)

           for key, value in data["current"].items():
               print(key + ":", value)

           engine.runAndWait()

