## MyBot — Python Chatbot

A beginner-friendly, rule-based chatbot built with Python. MyBot responds to predefined questions, uses a JSON file as its knowledge source, and handles unknown messages with a fallback response.

### Features

- Interactive command-line conversation
- Predefined question-and-answer responses
- Case-insensitive message handling
- Basic keyword matching
- JSON-based knowledge storage
- Error handling for missing or invalid knowledge files
- Unit tests using Python's built-in unittest framework

### Requirements

- Python 3
- Git (optional, for version control)
  No external Python packages are required.

### Installation

Clone the repository:
`git clone https://github.com/Ad-Abhishek/MyBot.git`

Navigate into the project:
`cd MyBot`

Create a virtual environment:
`python -m venv .venv`

Activate it on Windows Command Prompt:
`.venv\Scripts\activate.bat`

### Run the chatbot

`python main.py`

### Run tests

`python -m unittest -v`

### Project structure

MyBot/
├── main.py
├── knowledge.json
├── test_chatbot.py
├── .gitignore
└── README.md

### Technologies

- Python
- JSON
- Git
- GitHub
- unittest

### Future improvements

- More flexible natural language processing
- A graphical user interface
- A web-based chatbot
- AI model integration
- Conversation history
- Retrieval-Augmented Generation (RAG)
