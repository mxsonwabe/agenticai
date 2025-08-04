import os
import sys
from google import genai
from dotenv import load_dotenv

# get system arguments
ARGS = sys.argv

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model= "gemini-2.0-flash-001",
        contents= getArgs()
    )
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}.")
    print("Response:")
    print(response.text)

def getArgs():
    if (len(ARGS) < 2):
        print("No argument supplied.")
        print("Exiting...")
        sys.exit(1)
    str = ""
    for i in range(1, len(ARGS)):
        str += ARGS[i]
    return str

if __name__ == "__main__":
    main()
