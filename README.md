# Local Qwen Chatbot with Persistent Memory

A simple AI chatbot built using Python, Qwen3, Ollama, and SQLite.

## Features

- Runs Qwen3 locally using Ollama.
- Maintains conversation history during a session.
- Saves user-provided facts in an SQLite database.
- Retrieves saved facts after restarting the application.

## Technologies Used

- Python
- Qwen3 0.6B
- Ollama
- SQLite
- JSON and HTTP requests

## Requirements

- Python 3
- Ollama installed
- Qwen3 0.6B model downloaded

## Setup

1. Install Ollama from https://ollama.com/
2. Download the model:

   ```bash
   ollama run qwen3:0.6b
   ```

3. Make sure Ollama is running.
4. Run the chatbot:

   ```bash
   python qwen_test.py
   ```

## How to Use

- Enter a message to chat with Qwen.
- Type `remember: Your fact here` to save a fact.
- Ask questions about saved facts.
- Type `exit` to close the chatbot.

Saved facts are stored locally in `chat_memory.db`.

## Current Limitations

- Memory is based on explicitly saved facts, not automatic semantic retrieval.
- Response quality depends on the model.

## Future Improvements

- Add embedding-based semantic retrieval.
- Improve error handling.
- Add automated tests.
