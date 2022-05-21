import string
from nltk.corpus import stopwords


def clear_from_stopwords(message):
    text = ""
    russian_stopwords = stopwords.words("russian")
    for i in range(0, len(message)):
        if message[i] not in russian_stopwords:
            text += message[i]
            text += " "
    return text


def clear_message(message):
    string_punctuation = string.punctuation.replace('%', '')
    clean_text = message
    for ch in string_punctuation:
        clean_text = clean_text.replace(ch, "")
    return clean_text
