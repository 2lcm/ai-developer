from typing import TypedDict, Annotated, Optional  
import requests  
import asyncio  
from semantic_kernel.functions import kernel_function
import os
from dotenv import load_dotenv
import datetime

load_dotenv(override=True)

class WeatherPlugin:
    @kernel_function(description="Return the forecast weather at latitude and longitude location for up to 16 days")
    async def forecast_weather(
        self, 
        latitude:Annotated[str, "latitude of location"],
        longitude:Annotated[str, "longitude of location"],
        days:Annotated[int, "days to forecast"]
        ) -> dict:
        print(f"forecast weather location: {latitude}, {longitude}")
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,rain,showers,snowfall,weather_code,wind_speed_10m,wind_direction_10m,wind_gusts_10m&hourly=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation_probability,precipitation,rain,showers,snowfall,weather_code,cloud_cover,wind_speed_10m,uv_index&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&forecast_days={days}"
        response = requests.get(url)
        data = response.json()
        return data
    