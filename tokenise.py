import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
russian_stopwords = nltk.corpus.stopwords.words("russian")


def token_by_sentences(message):
    tokenized = sent_tokenize(message)
    return tokenized


def token_by_words(message):
    tokenized = word_tokenize(message)
    return tokenized
