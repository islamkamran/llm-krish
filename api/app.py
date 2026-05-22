#  for the system related APIs like chatbot, agent, vector database etc
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate # for the prompt template
from langchain_openai  import ChatOpenAI # because we are making complete chat models
from langserve import add_routes # for the langserve server as some APIs we will be hosting on langserve and some on fastapi and all the routes will be here
import uvicorn

import os
from dotenv import load_dotenv  # for loading environment variables from .env file

load_dotenv()  # load environment variables from .env file

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") # OPENAI api key


app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A Simple API Server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

# in the tutorials we have two different models for understanding purpose one online and other ollama llama2 offline but I will use mini and nano both online
model = ChatOpenAI(model = "gpt-4.1-mini")  # Mini
llm = ChatOpenAI(model = "gpt-4.1-nano")  # nano

#  Making two prompt
prompt1 = ChatPromptTemplate.from_template("write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("write me an poem about {topic} with 100 words")


add_routes(
    app,
    prompt1 | model,
    path = "/essay"
)

add_routes(
    app,
    prompt2 | llm,
    path = "/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port = 8000)