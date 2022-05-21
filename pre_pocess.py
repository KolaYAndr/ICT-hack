import lemmatise as lmm
import clearing_out as co
import tokenise as to
import spell_correct as sc


def preprocess(message):
    message = message.lower()
    message = co.clear_message(message)
    message = sc.spell(message)
    message = to.token_by_words(message)
    message = co.clear_from_stopwords(message)
    message = lmm.lemmatise(message)
    return message

