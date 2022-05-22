import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import tonization as ton
import pre_process as pp

def tell_ton(message):
    message = pp.preprocess(message)
    dictionary = ton.define_ton(message)
    df = pd.DataFrame(dictionary).T
    df = df.count()
    return df

def draw_emotions(message):
    message = pp.preprocess(message)
    dictionary = ton.define_ton(message)
    df = pd.DataFrame(dictionary).T
    df = df.count()

    fig, axis = plt.subplots(1, 1, figsize=(16, 8))
    sns.barplot(ax=axis, y=df.values, x=df.index, palette="Set1")
    return plt



def draw_bars_by_words(message):
    message = pp.preprocess(message)
    df = pd.DataFrame(message, columns={"word"})
    df["count"] = 1
    df = df.groupby('word', as_index=True)['count'].count()
    df = df.nlargest(5)

    fig, axis = plt.subplots(1, 1, figsize=(16, 8))
    sns.barplot(ax=axis, y=df, x=df.index, palette="Set1")
    return fig


def draw_bars_by_history(messages):
    df = pd.DataFrame(columns={'word'})
    for message in messages:
        message = pp.preprocess(message)
        temp = pd.DataFrame(message, columns={'word'})
        df = pd.concat([df, temp])
    df["count"] = 1
    df = df.groupby('word', as_index=True)['count'].count()
    df = df.nlargest(5)


    fig, axis = plt.subplots(1, 1, figsize=(16, 8))
    sns.barplot(ax=axis, y=df, x=df.index, palette="Set1")