from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import re
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# работаем по такой схеме:
# приведение к нижнему регистру
# удаление пунктуации
# исправляем ошибки
# токенизация
# удаление стоп-слов
# лемматизация
# определяем тон


X =["В меня со школы был влюблён парень. Ухаживал, делал подарки, заботился. " \
          "Я только смеялась над ним, отвергала. Однажды он даже заплакал. В итоге своей настойчивостью добился меня." \
          " Встречались, были счастливы. Неделю назад он меня бросил, не смог простить тех унижений. " \
          "Чувство собственного достоинства оказалось сильнее  любви. И я его понимаю. Я виновата сама. " \
          "Мужчины не прощают уязвлённого самолюбия."]

documents = []

stemmer = WordNetLemmatizer()

for sen in range(0, len(X)):
    # Удаление всех специальных символов
    document = re.sub(r'\W', ' ', str(X[sen]))

    # Удаление всех одиночных символов
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

    # Удаление единичных символов вначале
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

    # Удаление нескольких пробелов
    document = re.sub(r'\s+', ' ', document, flags=re.I)

    # Удаление префиксов b
    document = re.sub(r'^b\s+', '', document)

    # Нижний регистр
    document = document.lower()

    # Лемматизация
    document = document.split()

    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)

    documents.append(document)

# Мешон слов
vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('russian'))
X = vectorizer.fit_transform(documents).toarray()

# Поиск TFIDF
tfidfconverter = TfidfTransformer()
X = tfidfconverter.fit_transform(X).toarray()
with open('text_classifier', 'rb') as training_model:
    model = pickle.load(training_model)
y_pred2 = model.predict(X)

print(y_pred2)
# dai.draw_hist(message)
