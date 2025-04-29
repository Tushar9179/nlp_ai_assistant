import string
from sklearn.feature_extraction.text import CountVectorizer

# Initialize vectorizer (with English stopwords removal)
vectorizer = CountVectorizer(stop_words='english')


# Tokenize using CountVectorizer
def tokenize(text):
    return vectorizer.build_tokenizer()(text)


# Preprocess: Remove punctuation and lowercase the text
def preprocess(sentence):
    return sentence.translate(str.maketrans('', '', string.punctuation)).lower()


# Convert a sentence to a bag of words vector
def bag_of_words(text, vocab=None):
    # If vocab is passed, set it manually
    if vocab:
        vectorizer = CountVectorizer(vocabulary=vocab, stop_words='english')

    # Transform the text into a vector
    vector = vectorizer.transform([text]).toarray()
    return vector[0]


# if __name__ == "__main__":
#     sentence = "Hello, how are you doing?"
#     all_words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
#
#     preprocessed = preprocess(sentence)
#     tokenized = tokenize(preprocessed)
#
#     print("Tokenized:", tokenized)
#     print("Bag of Words:", bag_of_words(" ".join(tokenized), all_words))
