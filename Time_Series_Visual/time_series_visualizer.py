import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col=0,parse_dates=True)

# Clean data
df =df[(df['value'] < df['value'].quantile(.975)) & (df['value'] > df['value'].quantile(.025))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(16, 5))
    plt.plot(df.index, df['value'])
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df.index.year
    df_bar['Months'] = df.index.strftime('%B')
    df_grouped = df_bar.groupby(['Year', 'Months'])['value'].mean().reset_index()
    df_pivot = df_grouped.pivot(index='Year', columns='Months', values='value')
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
    df_pivot=df_pivot[month_order]
    # Draw bar plot
    fig = plt.figure(figsize=(10, 6))
    df_pivot.plot(kind='bar', ax=plt.gca(), legend=True)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Average Views per Month Grouped by Year')
    plt.tight_layout()
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['Year'] = df.index.year
    df_box['Months'] = df.index.strftime('%b')
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Converting the 'Month' column to an ordered categorical data type
    df_box['Months'] = pd.Categorical(df_box['Months'], categories=month_order, ordered=True)
    # Creating a figure and axes for the subplots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(40, 15))
    # Plotting box plots by year
    sns.boxplot(data=df_box, x='Year', y='value', ax=axes[0])
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    # Plotting box plots by month
    sns.boxplot(data=df_box, x='Months', y='value', ax=axes[1])
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    # Adjusting the layout and displaying the plots
    plt.tight_layout()
    # Draw box plots (using Seaborn)
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
