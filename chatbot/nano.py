# Step 1: Importing necessary libraries and setting up environment variables

from langchain_openai import ChatOpenAI  # first import should be model which company you are using openAI, Anthropic ...
from langchain_core.prompts import ChatPromptTemplate  # second import: As we will be entrying the prompts in templates this is also needed super important for chatbots
from langchain_core.output_parsers import StrOutputParser  # third import: As we will be getting the output in string format we need to parse it using this
# The above 3 are must

import streamlit as st  # for the UI of the chatbot
import os  # for accessing environment variables
from dotenv import load_dotenv  # for loading environment variables from .env file

load_dotenv()  # load environment variables from .env file

# step 2: Setting up environment variables for OpenAI and LangSmith API keys

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") # OPENAI api key

# the below is fopr langsmith for checking the tracing and debugging of the chatbot in langsmith dashboard
os.environ["LANGCHAIN_TRACING_V2"] = "true" 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") #LANGSMITH api key

# step 3: Setting up the prompt template for the chatbot
# Prompt template for the chatbot

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please reponse to the user queries"),
    ("user","Question:{question}")
])

# step 4: Setting up the Streamlit UI for the chatbot
st.title("Langchain Demo Project with OpenAI and LangSmith")
input_text = st.text_input("Enter your question here:")  # input box for user to enter their question

# step 5: Setting up the chatbot response logic calling the OpenAI model and getting the response
llm = ChatOpenAI(model="gpt-4.1-nano")
output_parser = StrOutputParser()

# step 6: chain them all

chain = prompt | llm | output_parser

if input_text:
    # the st.write is used to display the output of the chatbot in the Streamlit UI
    st.write(chain.invoke({"question": input_text}))