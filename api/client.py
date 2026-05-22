# for the client end points like web or mobile app
import requests
import streamlit as st


def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json={"input": {"topic": input_text}})
    
    return response.json()['output']['content']

def get_llm_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={"input": {"topic": input_text}})
    
    return response.json()['output']['content']

# making a streamlit UI for the client end
st.title("Langchain Client Open AI Mini and Nano")
input_text = st.text_input("What an Essay on....")
input_text1 = st.text_input("What a Poem on....")

# Handling the reponse from the API and displaying it in the UI
if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_llm_response(input_text1))