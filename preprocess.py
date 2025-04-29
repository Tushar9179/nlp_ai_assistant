import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# Set of common English stopwords
stop_words = set(stopwords.words('english'))


def clean_text(text, remove_stopwords=False):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Lowercase
    text = text.lower()
    # Split into words
    words = text.split()

    if remove_stopwords:
        words = [word for word in words if word not in stop_words]

    return ' '.join(words)


if __name__ == "__main__":
    sample = "Hello! This is just a TEST, with some random punctuation!!!"
    print("Original:", sample)
    print("Cleaned:", clean_text(sample, remove_stopwords=True))
