import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import tonization as ton

# доделаем мл, буду строить по нашему алгоритму


def draw_hist(message):
    dictionary = ton.define_ton(message)
    df = pd.DataFrame(dictionary).T
    df = df.count()
    info(df)
    fig, axis = plt.subplots(1, 1, figsize=(16, 8))
    sns.barplot(ax=axis, y=df.values, x=df.index, palette="Set1")
    plt.show()


def info(df):
    print(df)
