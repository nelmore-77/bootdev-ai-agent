import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

parser = argparse.ArgumentParser(description="A script that demonstrates command line flags")

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def arg_checker(arguments):
    if len(arguments) == 1 or len(arguments) > 3:
        print("Error: No Questions Asked")
        sys.exit(1)
    elif len(arguments) == 2 and "--verbose" in arguments:
        print("Error: No Questions Asked")
        sys.exit(1)
    else:
        pass


def main():
    arg_checker(sys.argv)
    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages,)
    print(response.text)

    if "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
