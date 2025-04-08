import openai

class SummarizeAgent:
    def __init__(self):
        openai.api_key = "your-key"

    async def run(self, context):
        text = context.get("input", "")
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Summarize this:\n{text}"}],
        )
        return response.choices[0].message.content
