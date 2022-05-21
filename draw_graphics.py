import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def draw_hist(dictionary):
    df = pd.DataFrame(dictionary).T
    # выкинем столбец skip, он всё равно ничего полезного не делает
    df = df.drop(labels='skip', axis=1)
    df = df.count()
    fig = px.histogram(df, x=df.index, y=df.values)
    fig.update_layout(title="Plot Title", xaxis_title="Тон", yaxis_title="Значение")
    fig.show()
