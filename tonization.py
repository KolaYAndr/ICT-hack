# Программа для тонализации текста

from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
FastTextSocialNetworkModel.MODEL_PATH = "fasttext-social-network-model.bin"


def define_ton(words):
    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)
    results = model.predict(words, k=1)
    for word, sentiment in zip(words, results):
        print(word, '->', sentiment)
