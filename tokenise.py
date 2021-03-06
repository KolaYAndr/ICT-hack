from rusenttokenize import ru_sent_tokenize
from nltk.tokenize import word_tokenize


def token_by_sentences(message):
    tokenized = ru_sent_tokenize(message)
    return tokenized


def token_by_words(message):
    tokenized = word_tokenize(message)
    return tokenized
