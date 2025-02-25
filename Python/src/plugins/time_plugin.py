from typing import TypedDict, Annotated, Optional  
import requests  
import asyncio  
from semantic_kernel.functions import kernel_function
import os
from dotenv import load_dotenv
import datetime

load_dotenv(override=True)

class TimePlugin:  

    @kernel_function(description="Return the current date time")
    async def current_datetime(self) -> str:
        now = str(datetime.datetime.now())
        return now

    @kernel_function(description="Return the Year for a date passed in as a parameter")
    async def get_year_of_date(self, date:Annotated[str, "The date format: mm/dd/YYYY"]) -> str:
        datetiem_val = datetime.datetime.strptime(date, "%m/%d/%Y")
        return str(datetiem_val.year)
    
    @kernel_function(description="Return the Month for a date passed in as a parameter")
    async def get_month_of_date(self, date:Annotated[str, "The date format: mm/dd/YYYY"]) -> str:
        datetiem_val = datetime.datetime.strptime(date, "%m/%d/%Y")
        return str(datetiem_val.month)
    
    @kernel_function(description="Return the Day of Week for a date passed in as a parameter")
    async def get_weekday_of_date(self, date:Annotated[str, "The date format: mm/dd/YYYY"]) -> str:
        datetiem_val = datetime.datetime.strptime(date, "%m/%d/%Y")
        return str(datetiem_val.weekday)
    