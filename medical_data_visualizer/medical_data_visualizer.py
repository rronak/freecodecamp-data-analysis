import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2 - Add overweight column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3 - Normalize cholesterol and glucose
df[['gluc', 'cholesterol']] = (df[['gluc', 'cholesterol']] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5 - Melt data
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    )

    # 6 - Create categorical plot
    fig = sns.catplot(
        data=df_cat,
        kind='count',
        x='variable',
        hue='value',
        col='cardio'
    ).set(ylabel='total').fig

    # 7 - Save and return figure
    fig.savefig('catplot.png')
    return fig


# 8
def draw_heat_map():
    # 9 - Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 10 - Calculate correlation matrix
    corr = df_heat.corr()

    # 11 - Mask upper triangle
    mask = np.triu(corr)

    # 12 - Create figure
    fig, ax = plt.subplots()

    # 13 - Draw heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='0.1f',
        square=True,
        ax=ax
    )

    # 14 - Save and return figure
    fig.savefig('heatmap.png')
    return fig

