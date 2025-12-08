import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color='blue', label='Data Points')


    # First line of best fit (all years)
    slope_all, intercept_all, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_all = pd.Series(range(df["Year"].min(), 2051))  # extend to 2050
    ax.plot(years_all, intercept_all + slope_all*years_all, 'r', label='Fit: all years')


    # Second line of best fit (year >= 2000)
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))  # extend to 2050
    ax.plot(years_recent, intercept_recent + slope_recent*years_recent, 'green', label='Fit: 2000+')

    # Add labels, title, legend
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # Save plot and return axes
    plt.savefig('sea_level_plot.png')
    return plt.gca()
