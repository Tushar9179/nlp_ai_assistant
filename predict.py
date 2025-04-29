import json
import os
import subprocess
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from bagofwords import tokenize, bag_of_words
from preprocess import clean_text
from commands.open_application import open_application  # Ensure you have this import

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
    cleaned_input = clean_text(user_input, remove_stopwords=True)
    tokenized_input = tokenize(cleaned_input)
    input_vector = bag_of_words(' '.join(tokenized_input), all_words).reshape(1, -1)

    best_score = 0
    best_tag = "unknown"
    best_example = ""

    for tokens, tag in documents:
        pattern_vector = bag_of_words(' '.join(tokens), all_words).reshape(1, -1)
        score = cosine_similarity(input_vector, pattern_vector)[0][0]
        if score > best_score:
            best_score = score
            best_tag = tag
            best_example = ' '.join(tokens)

    print(f"Best Match: {best_tag} with score: {best_score} (Input: '{user_input}')")

    return best_tag if best_score > 0 else "unknown", best_example


# Function to open any application based on user command
def open_application(app_name):
    try:
        if app_name.lower() == "calculator":
            subprocess.run("calc.exe")
        elif app_name.lower() == "steam":
            subprocess.run("steam")  # Ensure Steam is installed and in PATH
        elif app_name.lower() == "xbox":
            subprocess.run("xbox")  # Ensure Xbox app is installed and in PATH
        elif app_name.lower() == "notepad":
            subprocess.run("notepad.exe")
        elif app_name.lower() == "paint":
            subprocess.run("mspaint.exe")
        elif app_name.lower() == "wordpad":
            subprocess.run("write.exe")
        elif app_name.lower() == "cmd":
            subprocess.run("cmd")
        elif app_name.lower() == "control panel":
            subprocess.run("control")
        elif app_name.lower() == "task manager":
            subprocess.run("taskmgr")
        elif app_name.lower() == "explorer":
            subprocess.run("explorer")
        elif app_name.lower() == "registry editor":
            subprocess.run("regedit")
        elif app_name.lower() == "snipping tool":
            subprocess.run("snippingtool")
        elif app_name.lower() == "powershell":
            subprocess.run("powershell")
        elif app_name.lower() == "terminal":
            subprocess.run("wt")  # Windows Terminal
        elif app_name.lower() == "settings":
            subprocess.run("start ms-settings:", shell=True)
        elif app_name.lower() == "browser":
            subprocess.run("start chrome", shell=True)  # Ensure Chrome is in PATH
        elif app_name.lower() == "edge":
            subprocess.run("start msedge", shell=True)
        elif app_name.lower() == "internet explorer":
            subprocess.run("iexplore")
        elif app_name.lower() == "media player":
            subprocess.run("wmplayer")
        elif app_name.lower() == "word":
            subprocess.run("start winword", shell=True)  # Microsoft Word
        elif app_name.lower() == "excel":
            subprocess.run("start excel", shell=True)  # Microsoft Excel
        else:
            print(f"Unknown application command. I couldn't find a match for: {app_name}")
    except Exception as e:
        print(f"Error occurred while trying to open {app_name}: {e}")


# Function to execute the predicted intent
def execute_intent(intent, speech_text):
    speech_text = speech_text.lower()

    if intent == "open_application":
        open_application(speech_text)
    elif intent == "play_music":
        print("Playing music...")
        # Add functionality for playing music if needed
    else:
        print(f"Intent '{intent}' not recognized.")


# # Test the prediction in a loop
# if __name__ == "__main__":
#     while True:
#         inp = input("You: ")
#         if inp.lower() in ["quit", "exit"]:
#             break
#         intent, example = predict_intent(inp)
#         print(f"Predicted Intent: {intent}")
#         execute_intent(intent, inp)
