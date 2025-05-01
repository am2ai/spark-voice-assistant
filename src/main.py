from dotenv import load_dotenv
import os
from graph import build_conversation_graph
from voice import speak
import html

def main():
    load_dotenv()

    print("\nWelcome to S.P.A.R.K. — Your Speech-Powered Agent for Reasoning & Knowledge")
    print("Type your message to chat with the AI assistant. Responses will be spoken aloud if audio playback is available.")
    print("Type 'exit' to quit.\n")

    graph = build_conversation_graph()

    while True:
        user_input = input("You: ")
        user_input = html.escape(user_input.strip())
        if user_input.lower() in ["exit", "quit"]:
            break

        response = graph.invoke({"input": user_input})
        output = response.get("output", "")
        
        speak(output)

if __name__ == "__main__":
    main()