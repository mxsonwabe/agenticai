import os
import sys
import argparse
from google import genai
from dotenv import load_dotenv
from google.genai import types

parser = argparse.ArgumentParser(
    description = "CLI code agent"
)
group = parser.add_mutually_exclusive_group()

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    setUserPrompt()
    setFlags()

    args = parser.parse_args()
    # store message history
    if args.prompt:
        messages = [
           types.Content(
                role="user",
                parts=[types.Part(text=args.prompt)]
            ), 
        ]
        response = client.models.generate_content(
            model= "gemini-2.0-flash-001",
            contents= messages
        )
        displayResponse(args, verbose, args.prompt, response)

def setUserPrompt():
    parser.add_argument(
        "prompt",
        type = str,
        help = "message to pass to model"
    )

def setFlags():
    group.add_argument(
        "-v",
        "--verbose",
        help = "show more info",
        action = "store_true"
    )
    group.add_argument(
        '-q',
        "--quiet",
        help = "display output only",
        action = "store_true",
    )

def displayResponse(args, prompt: str, r):
    if args.verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {r.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {r.usage_metadata.candidates_token_count}")
        print(f"{r.text}")
    elif args.quiet:
        # print(f"user: {prompt}")
        # print(f"model: {r.text}")
        print(f"{r.text}")
    else:
        print(f"User: {prompt}")
        print(f"Model: {r.text}")


if __name__ == "__main__":
    main()
