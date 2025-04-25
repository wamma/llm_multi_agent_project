# main.py
import os, yaml
from fastapi import FastAPI
from schemas.mcp import MCPMessage
from broker import Broker
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scripts.analyze_mcp_logs import analyze

# providers 등록을 위해 wrapper 모듈을 반드시 import
import agents.openai_wrapper  
from agents.prompt_agent import PromptAgent

load_dotenv()
app = FastAPI()
broker = Broker()

# config/tasks.yaml 로딩
with open("config/tasks.yaml", encoding="utf-8") as f:
    tasks = yaml.safe_load(f)

# 모든 task를 PromptAgent로 자동 등록
for task_name, cfg in tasks.items():
    broker.register_agent(task_name, PromptAgent(template=cfg["template"]))

@app.post("/mcp")
async def process_message(message: MCPMessage):
    return await broker.handle(message)
