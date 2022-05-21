import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def draw_barplots(dictionary):
    df = pd.DataFrame(dictionary).T
    # выкинем столбец skip, он всё равно ничего полезного не делает
    df = df.drop(labels='skip', axis=1)
    df = df.sum()
    fig, axis = plt.subplots(1, 1, figsize=(16, 8))
    sns.barplot(ax=axis, y=df.values, x=df.index, palette="Set1")
    plt.show()
