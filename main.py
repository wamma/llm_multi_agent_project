from fastapi import FastAPI
from schemas.mcp import MCPMessage
from broker import Broker
from agents.summarize_agent import SummarizeAgent

app = FastAPI()
broker = Broker()
broker.register_agent("summarize", SummarizeAgent())

@app.post("/mcp")
async def process_message(message: MCPMessage):
    return await broker.handle(message)
