import clearing_out as co
import tokenise as to


message = "привет, ублюдки! Я срал вам в рты... Моя жопа болит"
# print(to.token_by_sentences(message) + "\n")
sms = to.token_by_words(message)
print(sms)


# def get_message(message):
#     return message

