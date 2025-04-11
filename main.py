from fastapi import FastAPI
from schemas.mcp import MCPMessage
from broker import Broker
from agents.summarize_agent import SummarizeAgent
from agents.translate_agent import TranslateAgent
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
broker = Broker()
broker.register_agent("summarize", SummarizeAgent())
broker.register_agent("translate", TranslateAgent())

@app.post("/mcp")
async def process_message(message: MCPMessage):
    return await broker.handle(message)