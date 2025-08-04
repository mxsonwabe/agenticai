import os
import sys
from google import genai
from dotenv import load_dotenv
from google.genai import types
from types import GenerateContentResponse

# get system arguments
ARGS = sys.argv

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    user_prompt = getUserPrompt()
    # store message history
    messages = [
       types.Content(role="user", parts=[types.Part(text=user_prompt)]), 
    ]
    response = client.models.generate_content(
        model= "gemini-2.0-flash-001",
        contents= messages
    )
    displayResponse(user_prompt,response)

def getUserPrompt():
    if (len(ARGS) < 2):
        print("No argument supplied.")
        print("Exiting...")
        sys.exit(1)
    str = ""
    for i in range(1, len(ARGS)):
        str += ARGS[i]
    return str

def displayResponse(user_prompt: str, r: GenerateContentResponse):
    print("Prompt tokens:", r.usage_metadata.prompt_token_count)
    print(f"Response tokens: {r.usage_metadata.candidates_token_count}.")
    print(f"user: {user_prompt}")
    print(f"model: {r.text}")

if __name__ == "__main__":
    main()
