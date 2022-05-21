from nltk.tokenize import word_tokenize
import clearing_out as co
from rusenttokenize import ru_sent_tokenize


def token_by_sentences(message):
    tokenized = ru_sent_tokenize(message)
    return tokenized


def token_by_words(message):
    message = message.lower()
    message = co.clear_message(message)
    tokenized = word_tokenize(message)
    return tokenized
