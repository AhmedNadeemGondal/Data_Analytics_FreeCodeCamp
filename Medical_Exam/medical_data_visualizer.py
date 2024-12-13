import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['weight'] / ((df['height']/100) ** 2)
df['overweight'] = (df['overweight'] >= 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot

def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'], var_name='variable', value_name='total')

    # df_cat = None
    
    # Draw the catplot with 'sns.catplot()'
    # Get the figure for the output
    fig = sns.catplot(data=df_cat, kind='count', x='variable', hue='total', col='cardio', col_wrap=2)
    fig.set_axis_labels("variable", "total")

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    #low blood pressure greater or equal to high blood pressure removed
    # df = pd.read_csv('medical_examination.csv')
    df1 = df[df['ap_lo'] <= df['ap_hi']]

    #Height below 2.5% and above 97.5% removed
    df1 = df1[(df1['height'] >= df1['height'].quantile(0.025)) & (df1['height'] <= df1['height'].quantile(0.975))]

    #Weight below 2.5% and above 97.5% removed
    df_heat = df1[(df1['weight'] >= df1['weight'].quantile(0.025)) & (df1['weight'] <= df1['weight'].quantile(0.975))]
    

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    masked_corr_matrix = corr.mask(mask)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(data=masked_corr_matrix, annot=True, fmt=".1f", cmap="coolwarm", cbar_kws={"shrink": 0.8}, ax=ax)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
