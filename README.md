
# Virtual Assistant

A Python-based virtual assistant that uses natural language processing (NLP) and machine learning to understand user input, predict intents, and perform actions such as opening applications, responding with predefined responses, and playing music.

## Features

- **Speech Input**: The assistant can listen to commands via microphone and execute tasks accordingly.
- **Text Input**: The assistant can also respond to text input.
- **Intent Recognition**: Using a custom-trained model and bag-of-words technique, the assistant predicts the intent of user input.
- **Action Execution**: Depending on the intent, the assistant can open applications (like Chrome, Calculator) or respond with predefined messages.
- **Customizable Intents and Responses**: Intents and corresponding responses are stored in a JSON file, making it easy to add new functionalities.

## Table of Contents

- [Installation](#installation)
- [File Structure](#file-structure)
- [Usage](#usage)
  - [Run the Virtual Assistant](#run-the-virtual-assistant)
  - [Text Input](#text-input)
  - [Voice Input](#voice-input)
  - [Exit the Assistant](#exit-the-assistant)
- [How It Works](#how-it-works)
  - [Intent Recognition](#intent-recognition)
  - [Actions](#actions)
  - [Example Intent](#example-intent)
  - [Execution Example](#execution-example)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/virtual-assistant.git
cd virtual-assistant
```

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

Ensure that you have the necessary files:

- `intents.json` (contains intents, patterns, and responses)
- `commands/` folder (contains functions to execute specific actions)
- `speech_input.py` and `speech_output.py` for handling speech recognition and synthesis.

## File Structure

The project is organized as follows:

```bash
virtual-assistant/
├── commands/
│   ├── open_application.py      # Contains functions to open applications
├── intents.json                 # Contains intents, patterns, and responses
├── bagofwords.py                # Tokenizer and bag-of-words functionality
├── predict.py                   # Functions for predicting intent
├── preprocess.py                # Data cleaning and preprocessing
├── speech_input.py              # Speech recognition module
├── speech_output.py             # Speech synthesis module
└── main.py                      # Main entry point to start the assistant
```

## Usage

### Run the Virtual Assistant

To start the virtual assistant, run the `main.py` file:

```bash
python main.py
```

The assistant will prompt you to choose an input method (either text or voice).

### Text Input

1. Choose option 1 for text input.
2. Type your query, e.g., "hello", "open calculator", or "play music".
3. The assistant will predict the intent and either respond with a message or execute the corresponding action.

### Voice Input

1. Choose option 2 for voice input.
2. Speak a command, such as "open chrome" or "how are you".
3. The assistant will process the speech and provide a response or take action.

### Exit the Assistant

To exit the assistant, type `quit` or `exit` in text input mode or say `quit` or `exit` in voice input mode.

## How It Works

### Intent Recognition

- **Bag of Words**: The assistant uses a custom bag-of-words model to convert user input into a vector and compares it with predefined patterns to predict the intent.
- **Cosine Similarity**: The input is compared with the stored patterns using cosine similarity to determine the best match.

### Actions

- If the predicted intent is `open_application`, the assistant looks up the command in a predefined dictionary (`app_commands`) and opens the corresponding application using functions from the `commands/open_application.py` file.
- If the intent is something else (like greeting), the assistant simply selects a response from the `responses` list defined in `intents.json`.

### Example Intent

Here’s an example of an intent from `intents.json`:

```json
{
  "tag": "greeting",
  "patterns": [
    "hello",
    "hi",
    "hey",
    "good morning",
    "good evening",
    "how are you",
    "what's up"
  ],
  "responses": [
    "Hello! How can I assist you today?",
    "Hi there! What can I do for you?",
    "Good day! How may I help you?"
  ]
}
```

### Execution Example

**User Input**: "open calculator"

**Predicted Intent**: `open_application`

**Response**: The assistant opens the Calculator application.

## Commands

The assistant can handle the following commands:

- `open_application`: Open predefined applications (e.g., Calculator, Chrome, Word).
- `play_music`: Respond with a message indicating that music will be played.
- `greeting`: Respond with a greeting message.

You can add new commands and responses in the `intents.json` file.

## Contributing

If you have any suggestions or improvements, feel free to fork this repository and create a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
