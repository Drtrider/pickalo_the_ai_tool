import os
import sys
from dotenv import load_dotenv
from google import genai


def main():
    print("Main started!")
    
    # Check and manage arguments passed into main.py
    if len(sys.argv) == 2:
        user_prompt = sys.argv[1]
    elif len(sys.argv) == 1:
        print("ERROR: No input prompt argument provided.")
        sys.exit(1)
    else:
        print("ERROR: Too many aguments given!")
        sys.exit(1)

    # Import api key from env
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Initialize Google GenAI Client
    client = genai.Client(api_key=api_key)

    # Genereate some content
    response = client.models.generate_content(
        model = "gemini-2.0-flash-001",
        contents = user_prompt
    )

    # Return content
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
