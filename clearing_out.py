import string


def clear_message(message):
    string.punctuation
    clean_text = message
    for ch in string.punctuation:
        clean_text = clean_text.replace(ch, "")
    return clean_text

