import string
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.preprocessing import FunctionTransformer
from collections import Counter

# Tokenize the sentence into words (Remove punctuation and split by spaces)
def tokenize(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.split()

# Simple stemming function that takes a word and returns its "root" form
# This is just a basic approach for demonstration (use a more advanced method if needed)
def simple_stem(word):
    # Basic approach: remove 'ing', 'ed', etc.
    if word.endswith('ing'):
        return word[:-3]
    if word.endswith('ed'):
        return word[:-2]
    return word

# Clean the sentence by removing stopwords and punctuation
def clean_text(text, remove_stopwords=False):
    # Tokenize text
    tokens = tokenize(text)

    # Remove stopwords if needed
    if remove_stopwords:
        tokens = [word for word in tokens if word.lower() not in ENGLISH_STOP_WORDS]

    # Apply basic stemming
    tokens = [simple_stem(word.lower()) for word in tokens]

    return ' '.join(tokens)
#
# if __name__ == "__main__":
#     sample = "Hello! This is just a TEST, with some random punctuation!!!"
#     print("Original:", sample)
#     print("Cleaned:", clean_text(sample, remove_stopwords=True))
