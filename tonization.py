import draw_graphics as dg
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
FastTextSocialNetworkModel.MODEL_PATH = "fasttext-social-network-model.bin"


def define_ton(words):
    dictionary = dict()
    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)
    results = model.predict(words, k=1)
    for word, sentiment in zip(words, results):
        dictionary[word] = sentiment
    dg.draw_hist(dictionary)