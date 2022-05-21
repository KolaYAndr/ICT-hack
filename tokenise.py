from nltk.tokenize import word_tokenize, sent_tokenize
import nltk

nltk.download('stopwords')
nltk.download('punkt')

def token_by_sentences(message):
    tokenized = sent_tokenize(message)
    return tokenized


def token_by_words(message):
    tokenized = word_tokenize(message)
    return tokenized
