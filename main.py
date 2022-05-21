import prepocess as pp

# работаем по такой схеме:
# приведение к нижнему регистру
# удаление пунктуации
# токенизация
# удаление стоп-слов
# лемматизация


message = input()
message = pp.preprocess(message)
print(message)
