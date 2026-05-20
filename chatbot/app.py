from langchain_openai import ChatOpenAI  # first import should be model which company you are using openAI, Anthropic ...
from langchain_core.prompts import ChatPromptTemplate  # second import: As we will be entrying the prompts in templates this is also needed super important for chatbots
from langchain_core.output_parsers import StrOutputParser  # third import: As we will be getting the output in string format we need to parse it using this
# The above 3 are must

import streamlit as st  # for the UI of the chatbot
import os  # for accessing environment variables
from dotenv import load_dotenv  # for loading environment variables from .env file

load_dotenv()  # load environment variables from .env file

print("Application is Working...")  