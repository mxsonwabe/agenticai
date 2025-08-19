import os
import sys
import argparse
from google import genai
from dotenv import load_dotenv
from google.genai import types
from functions.get_files_info import available_function

parser = argparse.ArgumentParser(
    description="CLI code agent"
)
group = parser.add_mutually_exclusive_group()

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons
"""


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
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_function], # feed available tool to LLM
                system_instruction=system_prompt,
            )
        )
        displayResponse(args, args.prompt, response)


def setUserPrompt():
    parser.add_argument(
        "prompt",
        type=str,
        help="message to pass to model"
    )


def setFlags():
    group.add_argument(
        "-v",
        "--verbose",
        help="show more info",
        action="store_true"
    )
    group.add_argument(
        '-q',
        "--quiet",
        help="display output only",
        action="store_true",
    )


def displayResponse(args, prompt: str, response):
    if args.verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {
              response.usage_metadata.candidates_token_count}")
        if response.function_calls:
            for function_call_part in response.function_calls:
                print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        else:
            print(f"{response.text}")
    elif args.quiet:
        # print(f"user: {prompt}")
        # print(f"model: {r.text}")
        print(f"{response.text}")
    else:
        print(f"User: {prompt}")
        if response.function_calls:
            for function_call_part in response.function_calls:
                print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        else:
            print(f"Model: {response.text}")


if __name__ == "__main__":
    main()
