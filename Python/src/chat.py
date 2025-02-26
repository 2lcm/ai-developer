import asyncio
import logging
from dotenv import load_dotenv
from semantic_kernel.utils.logging import setup_logging
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, OpenAITextToImage
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.connectors.openapi_plugin import OpenAPIFunctionExecutionParameters
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.functions import KernelArguments

from plugins.geo_coding_plugin import GeoPlugin
from plugins.weather_plugin import WeatherPlugin
from plugins.time_plugin import TimePlugin
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)

# Add Logger
logger = logging.getLogger(__name__)

load_dotenv(override=True)

chat_history = ChatHistory()

def initialize_kernel():
    #Challene 02 - Add Kernel
    kernel = Kernel()
    #Challenge 02 - Chat Completion Service
    chat_completion = AzureChatCompletion(service_id="gpt-4o-mini")
    #Challenge 02- Add kernel to the chat completion service
    kernel.add_service(chat_completion)

    setup_logging()
    logging.getLogger("kernel").setLevel(logging.DEBUG)

    return kernel


async def process_message(user_input):
    kernel = initialize_kernel()

    #Challenge 03 and 04 - Services Required
    #Challenge 03 - Create Prompt Execution Settings
    execution_settings = AzureChatPromptExecutionSettings(temperature=0)
    execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()


    # Challenge 03 - Add Time Plugin
    # Placeholder for Time plugin
    kernel.add_plugin(TimePlugin(), plugin_name="Time")
    # kernel.add_plugin(WeatherPlugin(), plugin_name="Weather")
    # kernel.add_plugin(GeoPlugin(), plugin_name="Geometry")

    # Challenge 04 - Import OpenAPI Spec
    # Placeholder for OpenAPI plugin
    # kernel.add_plugin_from_openapi(
    #     plugin_name="get_tasks",
    #     openapi_document_path="http://127.0.0.1:8000/openapi.json",
    #     execution_settings=OpenAPIFunctionExecutionParameters(
    #         enable_payload_namespacing=True,
    #     )
    # )


    # Challenge 05 - Add Search Plugin


    # Challenge 06- Semantic kernel filters

    # Challenge 07 - Text To Image Plugin
    # Placeholder for Text To Image plugin

    # Start Challenge 02 - Sending a message to the chat completion service by invoking kernel
    chat_history.add_user_message(user_input)

    chat_completion = kernel.get_service(service_id="gpt-4o-mini")
    result = await chat_completion.get_chat_message_content(
        chat_history=chat_history,
        settings=execution_settings,
        kernel=kernel,
        arguments=KernelArguments(),
    )
    chat_history.add_message(result)

    return result

def reset_chat_history():
    global chat_history
    chat_history = ChatHistory()