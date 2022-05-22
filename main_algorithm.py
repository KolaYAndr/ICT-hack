import numpy as np
import re
import nltk
from sklearn.datasets import load_files
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pandas as pd

df1 = pd.read_csv('dataset_final .csv', usecols=['data'])
df2 = pd.read_csv('dataset_final .csv', usecols=['target'])

df = df1.values[1:350]
DF = df2.values[1:350]


strings = []
list_of_y = []
for i in range(1, len(df)):
    strings.append(df[i][0])
    list_of_y.append(DF[i][0])


# загрузка доков/сообщений

X, y = strings, list_of_y # Х - сами строки, у - массив из 0 или 1, соответствующие классам

# Обработка
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

# Создание наборов для обучения и тестирования
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print(X_test)
# Создание обучающей модели
# Классификатор случайного леса
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit(X_train, y_train)
# Prediction
y_pred = classifier.predict(X_test)

# Оценка модели (матрица путаницы и мера F1)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

# Сохранение и загрузка модели
with open('text_classifier', 'wb') as picklefile:
   pickle.dump(classifier, picklefile)

# Загрузка модели в другом файле
with open('text_classifier', 'rb') as training_model:
    model = pickle.load(training_model)
y_pred2 = model.predict(X_test)
print(y_pred2)
print(confusion_matrix(y_test, y_pred2))
print(classification_report(y_test, y_pred2))
print(accuracy_score(y_test, y_pred2))
#
#