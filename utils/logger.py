#utils/logger.py
import json, time
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request

app = FastAPI()

class MCPLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path == "/mcp" and request.method == "POST":
            body = await request.json()
            task = body.get("task")
            keys = list(body.get("context", {}).keys())
            log_entry = {
                "ts": time.time(),
                "task": task,
                "keys": keys
            }
            # 1) 파일로 쌓기
            with open("logs/mcp_requests.log", "a", encoding="utf-8") as f:
                f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
            # 2) 또는 DB에 저장하기
            # save_to_db(task, keys, log_entry["ts"])
        return await call_next(request)

app.add_middleware(MCPLoggingMiddleware)