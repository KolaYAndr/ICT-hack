import lemmatise as lmm
import clearing_out as co
import tokenise as to


def preprocess(message):
    message = message.lower()
    message = co.clear_message(message)
    message = to.token_by_words(message)
    message = co.clear_from_stopwords(message)
    message = lmm.lemmatise(message)
    return message
