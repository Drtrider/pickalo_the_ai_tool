import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def setup_arguments():
    """Uses argparse to return a neat little object, that holds the arguments passed into main."""

    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Generate content using Google GenAI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
        Examples:
        python main.py "Write a poem about cats"
        python main.py "Explain quantum physics" --verbose
        """
    )

    # Add required positional argument
    parser.add_argument(
        "prompt",
        help="The prompt to send to the AI model"
    )

    # Add optional arguments for future use
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output"
    )

    parser.add_argument(
        "--model",
        default="gemini-2.0-flash-001",
        help="AI model to use (default: gemini-2.0-flash-001)"
    )

    return parser.parse_args()


def main():
    print("Main started!")

    # Setup arguments
    args = setup_arguments()

    if args.verbose:
        print(f"Using model: {args.model}")
        print(f"Prompt: {args.prompt}")

    # Import api key from env
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Initialize Google GenAI Client
    client = genai.Client(api_key=api_key)

    # Create list of content
    messages = [
        types.Content(role="user", parts=[types.Part(text=args.prompt)])
    ]

    # Genereate some content
    response = client.models.generate_content(
        model=args.model,
        contents=messages
    )

    # Return content
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
