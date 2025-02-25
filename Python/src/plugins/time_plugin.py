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
        print(datetime.datetime.now())
        now = str(datetime.datetime.now())
        print(now)
        return now
    