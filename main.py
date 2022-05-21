import prepocess as pp
import tonization as ton

# работаем по такой схеме:
# приведение к нижнему регистру
# удаление пунктуации
# токенизация
# удаление стоп-слов
# лемматизация
# определяем тон


message = "работал слишком много"
# message = input()
message = pp.preprocess(message)
ton.define_ton(message)
