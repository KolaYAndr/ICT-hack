from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import nltk
from nltk.tokenize import word_tokenize
from razdel.segmenters.tokenize import punct

nltk.download('punkt')
poem = '''
По морям, играя, носится
с миноносцем миноносица.
Льнет, как будто к меду осочка,
к миноносцу миноносочка.
И конца б не довелось ему,
благодушью миноносьему.
Вдруг прожектор, вздев на нос очки,
впился в спину миноносочки.
Как взревет медноголосина:
Р-р-р-астакая миноносина!
'''
sw = stopwords.words("russian")
words = [w.strip(punct).lower() for w in word_tokenize(poem)]
words = [w for w in words if w not in sw and w != '']

snowball = SnowballStemmer("russian")

for w in words:
    print("%s: %s" % (w, snowball.stem(w)))