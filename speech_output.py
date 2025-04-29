import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Function to speak the text
def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

# Example usage
# if __name__ == "__main__":
#     text = "Hello, how can I assist you today?"
#     print(f"Speaking: {text}")
#     speak(text)
