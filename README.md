# Pickalo

A command-line AI content generator built with Python and Google's GenAI SDK. This project is used during the boot.dev course, and is a simple-smooth-brained version of something like claude code. (Aparantly.)

## 🎯 Purpose

This is a practice repository created as part of the [boot.dev](https://boot.dev) learning journey. It showcases:
- Modern Python CLI development with `argparse`
- Google GenAI SDK integration

## ✨ Features

- **AI Content Generation**: Generate text content using Google's Gemini models
- **Flexible Model Selection**: Choose from different Gemini models
- **Verbose Output**: Optional detailed information about token usage
- **Environment-based Configuration**: Secure API key management
- **Modern CLI Interface**: Clean argument parsing with help documentation

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- Google GenAI API key

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd pickalo
   ```

2. Install dependencies using uv (recommended) or pip:
   ```bash
   # Using uv
   uv sync
   
   # Or using pip
   pip install -e .
   ```

3. Set up your environment variables:
   ```bash
   # Create a .env file in the project root
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

### Getting Your API Key

1. Visit the [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file

## 📖 Usage

### Basic Usage

Generate content with a simple prompt:
```bash
python main.py "Write a poem about cats"
```

### Advanced Usage

Use verbose mode to see token usage:
```bash
python main.py "Explain quantum physics" --verbose
```

Specify a different model:
```bash
python main.py "Tell me a joke" --model gemini-2.0-flash-001
```

### Command-Line Options

- `prompt` (required): The text prompt to send to the AI
- `--verbose, -v`: Enable verbose output showing token usage
- `--model`: Specify the Gemini model to use (default: gemini-2.0-flash-001)
- `--help, -h`: Show help message and exit

## 🛠️ Development

### Project Structure

```
pickalo/
├── main.py           # Main application entry point
├── pyproject.toml    # Project configuration and dependencies
├── uv.lock          # Dependency lock file
├── .env             # Environment variables (create this)
├── .gitignore       # Git ignore patterns
└── README.md        # This file
```

### Key Components

- **`setup_arguments()`**: Handles CLI argument parsing using `argparse`
- **`main()`**: Core application logic for API interaction
- **Environment Management**: Uses `python-dotenv` for secure API key handling

### Dependencies

- `google-genai==1.12.1`: Google's GenAI SDK
- `python-dotenv==1.1.0`: Environment variable management

## 🎓 Learning Objectives

This project demonstrates several important concepts:

1. **Introduce you to multi-directory Python projects**
2. **Understand how the AI tools that you'll almost certainly use on the job actually work under the hood**
3. **Practice your Python and functional programming skills**

## 🤝 Contributing

This is a learning project, but feel free to:
- Report issues or bugs
- Suggest improvements
- Share your own implementations

## 🔗 Resources

- [Google GenAI SDK Documentation](https://ai.google.dev/api/python)
- [argparse Documentation](https://docs.python.org/3/library/argparse.html)
- [boot.dev](https://boot.dev) - Learn backend development
- [Python Packaging Guide](https://packaging.python.org/en/latest/)

---

*"Built with 🫠 as part of my boot.dev learning journey. -- Drt "*