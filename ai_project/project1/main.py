from langchain_core.messages import HumanMessage # What it is: Formats user messages for AI
from langchain_openai import ChatOpenAI # What it is: AI model client
from langchain.tools import tool # What it is: Tools for AI to use
from langgraph.prebuilt import create_react_agent # What it is: Creates a reactive agent
from dotenv import load_dotenv # What it is: Loads environment variables from .env file
import os # What it is: Python standard library for interacting with the operating system

load_dotenv() # Load environment variables from .env file

@tool
def calculator(a:float , b:float) -> str:
    """Add two numbers"""
    return str(a + b)

def main():
    model = ChatOpenAI(
        base_url="https://api.groq.com/openai/v1", # Think: "Which phone number am I calling?"
        api_key=os.getenv("GROQ_API_KEY"), # Think: "Do I have permission to call?"
        model="llama-3.1-8b-instant", # Think: "What phone number am I calling?"
        temperature=0 # Think: "How should I phrase my call?"
    )

    tools = [calculator]

    agent_executer = create_react_agent(model, tools) #create a react agent

    print("welcome i am your ai assestient enter quit to exit")

    while True:
        user_input = input("You:").strip() #remove leading and trailing whitespace

        if user_input == "quit":
            break

        print("\nAssistant:", end="") #dont go to the next line
        for chunk in agent_executer.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
            print()


if __name__ == "__main__":
    main()

                
