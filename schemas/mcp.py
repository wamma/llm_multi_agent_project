from pydantic import BaseModel
from typing import Dict, Optional

class MCPMessage(BaseModel):
    role: str
    task: str
    context: Dict
    metadata: Optional[Dict] = {}