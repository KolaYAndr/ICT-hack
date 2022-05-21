import tokenise


message = "привет, ублюдки! Я срал вам в рты... Моя жопа болит"

print(tokenise.token_by_sentences(message))
sms = tokenise.token_by_words(message)
print(sms)


