import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
russian_stopwords = nltk.corpus.stopwords.words("russian")


# def token_by_sentences(message):
#     tokenised = sent_tokenise(message)
#     return tokenised

def token_by_words(message):
    tokenised = word_tokenize(message)
    return tokenised