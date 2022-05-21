import tokenise
import pandas as pd
from corus import load_rudrec

text = input()
records = tokenise.token_by_sentences(text)
print(records)
data = []
for record in records:
    data.append(record)
print(data)
df = pd.DataFrame(data, columns=['text'])
df.head()
