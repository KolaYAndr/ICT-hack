import lemmatise as lmm
import clearing_out as co
import tokenise as to

#приведение к нижнему регистру
#токенизация
#удаление пунктуации
#лемматизация
#удаление стоп-слов

message = "Привет, ублюдки! Я срал вам в рты... Моя жопа болит"
message = message.lower()
message = co.clear_message(message)
message = to.token_by_words(message)
message = co.clear_from_stopwords(message)
#message = lmm.lemmatise(message)
print(message)
