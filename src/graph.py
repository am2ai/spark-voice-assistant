from typing import TypedDict

class ConversationState(TypedDict):
    input: str
    output: str

from langgraph.graph import StateGraph, END
from openai import OpenAI
import os

class Agent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def run(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful and expressive voice assistant named S.P.A.R.K."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

def build_conversation_graph():
    agent = Agent()

    def handle_prompt(state: dict) -> dict:
        user_input = state.get("input", "")
        reply = agent.run(user_input)
        return {"output": reply}

    builder = StateGraph(ConversationState)
    builder.add_node("respond", handle_prompt)
    builder.set_entry_point("respond")
    builder.set_finish_point("respond")
    
    return builder.compile()