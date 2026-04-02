from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

API_KEY = "7c49591665c3b7d90de8b57391b3260b"  # get from openweathermap.org

class CityInput(BaseModel):
    city: str

@app.get("/")
def home():
    return {"message": "Weather AI App"}

@app.post("/weather")
def get_weather(data: CityInput):
    city = data.city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    result = response.json()

    temp = result["main"]["temp"]

    # simple AI logic
    if temp > 25:
        advice = "It's hot! Wear light clothes."
    elif temp < 10:
        advice = "It's cold! Wear a jacket."
    else:
        advice = "Weather is nice!"

    return {
        "city": city,
        "temperature": temp,
        "advice": advice
    }