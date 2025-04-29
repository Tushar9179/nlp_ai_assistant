import json
import random
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from bagofwords import tokenize, bag_of_words  # Assuming you have the bag_of_words function ready
from speech_input import listen_for_command  # Assuming this is your speech-to-text input function
from speech_output import speak  # Assuming this is your text-to-speech output function
import subprocess
from commands.open_application import open_application
from preprocess import clean_text
# Load intents from JSON file
with open("intents.json", "r") as file:
    intents = json.load(file)["intents"]

# Build vocabulary and documents for training
all_words = []
documents = []

# Tokenize and clean patterns
for intent in intents:
    for pattern in intent["patterns"]:
        cleaned = clean_text(pattern, remove_stopwords=True)
        tokens = tokenize(cleaned)
        all_words.extend(tokens)
        documents.append((tokens, intent["tag"]))

# Remove duplicates and sort the vocabulary
all_words = sorted(set(all_words))

# Function to predict intent based on user input
def predict_intent(user_input):
    # Clean and tokenize the input
    cleaned_input = clean_text(user_input, remove_stopwords=True)
    tokenized_input = tokenize(cleaned_input)
    input_vector = bag_of_words(' '.join(tokenized_input), all_words).reshape(1, -1)

    # Variables to keep track of the best match
    best_score = 0
    best_tag = "unknown"
    best_example = ""
    best_response = ""

    # Compare input with each pattern in the documents
    for tokens, tag in documents:
        pattern_vector = bag_of_words(' '.join(tokens), all_words).reshape(1, -1)
        score = cosine_similarity(input_vector, pattern_vector)[0][0]
        if score > best_score:
            best_score = score
            best_tag = tag
            best_example = ' '.join(tokens)

    # Get the response associated with the best intent
    for intent in intents:
        if intent["tag"] == best_tag:
            best_response = random.choice(intent["responses"])

    # Return the predicted tag, response, and example
    return best_tag, best_response, best_example

# Function to handle dynamic application opening
def execute_intent(intent, speech_text):
    if intent == "open_application":
        # Normalize the speech text to lowercase for easier matching
        speech_text = speech_text.lower()

        # Define a mapping between phrases and actual application names
        app_commands = {
            "calculator": ["calculator", "open calculator", "start calculator"],
            "chrome": ["chrome", "open chrome", "start chrome", "open google chrome"],
            "notepad": ["notepad", "open notepad", "start notepad"],
            "word": ["word", "open word", "start word", "open microsoft word"],
            "excel": ["excel", "open excel", "start excel", "open microsoft excel"],
            "youtube": ["youtube", "open youtube", "start youtube"],
            "steam": ["steam", "open steam", "start steam"],
            "xbox": ["xbox", "open xbox", "start xbox"],
            "paint": ["paint", "open paint", "start paint", "open mspaint"],
            "wordpad": ["wordpad", "open wordpad", "start wordpad"],
            "cmd": ["cmd", "command prompt", "open cmd", "start command prompt"],
            "control panel": ["control panel", "open control panel", "start control panel"],
            "task manager": ["task manager", "open task manager", "start task manager"],
            "explorer": ["explorer", "open file explorer", "start explorer"],
            "registry editor": ["registry editor", "open registry editor", "start regedit"],
            "snipping tool": ["snipping tool", "open snipping tool", "start snipping tool"],
            "powershell": ["powershell", "open powershell", "start powershell"],
            "terminal": ["terminal", "open terminal", "start terminal", "open windows terminal"],
            "settings": ["settings", "open settings", "start settings"],
            "edge": ["edge", "microsoft edge", "open edge", "open microsoft edge"],
            "internet explorer": ["internet explorer", "open internet explorer", "start internet explorer"],
            "media player": ["media player", "windows media player", "open media player", "start media player"],
            "spotify": ["spotify", "open spotify", "start spotify"],
            "discord": ["discord", "open discord", "start discord"],
            "slack": ["slack", "open slack", "start slack"]
        }

        # Iterate through the app_commands dictionary and find a match
        for app, phrases in app_commands.items():
            if any(phrase in speech_text for phrase in phrases):
                open_application(app)  # Open the corresponding application
                speak(f"Opening {app} now.")  # Let the user know what is happening
                return  # Exit once the correct application is opened

        # If no match found
        speak(f"Application command '{speech_text}' not recognized!")

# Function to just respond from the responses list
def respond(intent):
    for intent_data in intents:
        if intent_data["tag"] == intent:
            response = random.choice(intent_data["responses"])
            speak(response)  # Speak the response
            return

def main():
    print("🎤 Virtual Assistant is ready!")

    # Ask the user for the input method (1 for text, 2 for voice)
    while True:
        input_method = input("Choose input method (1 for Text, 2 for Voice): ").strip()

        if input_method == "1":
            print("You selected text input. Type 'quit' to exit.")
            while True:
                # Get text input from the user
                user_input = input("You: ")

                # Check if the user wants to quit
                if user_input.lower() in ["quit", "exit"]:
                    speak("Goodbye!")
                    return  # Exit the function

                # Predict intent based on the user's input
                intent, response, example = predict_intent(user_input)

                # Print predicted intent, response, and example
                print(f"Predicted Intent: {intent}")
                print(f"Response: {response}")
                print(f"Example: {example}")

                # Check if the intent is for an action like opening an application
                if intent == "open_application":
                    execute_intent(intent, user_input)
                else:
                    # For other intents, just respond with a message from the response list
                    respond(intent)

        elif input_method == "2":
            print("You selected voice input. Say 'quit' to exit.")
            while True:
                # Get speech input from the user
                user_input = listen_for_command()
                print(f"You said: {user_input}")

                # Check if the user wants to quit
                if user_input.lower() in ["quit", "exit"]:
                    speak("Goodbye!")
                    return  # Exit the function

                # Predict intent based on the user's input
                intent, response, example = predict_intent(user_input)

                # Print predicted intent, response, and example
                print(f"Predicted Intent: {intent}")
                print(f"Response: {response}")
                print(f"Example: {example}")

                # Check if the intent is for an action like opening an application
                if intent == "open_application":
                    execute_intent(intent, user_input)
                else:
                    # For other intents, just respond with a message from the response list
                    respond(intent)

        else:
            print("Invalid input. Please choose 1 for Text or 2 for Voice.")

if __name__ == "__main__":
    main()
