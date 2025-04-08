class Broker:
    def __init__(self):
        self.registry = {}

    def register_agent(self, task: str, agent):
        self.registry[task] = agent

    async def handle(self, message):
        task = message.task
        agent = self.registry.get(task)
        if not agent:
            return {"error": f"No agent found for task '{task}'"}
        return await agent.run(message.context)
