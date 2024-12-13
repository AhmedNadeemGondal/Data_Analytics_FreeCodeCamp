import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create the scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create a range of years up to 2050
    years = range(df['Year'].min(), 2051)

    # Calculate the corresponding sea level values using the regression equation
    sea_level = slope * years + intercept

    # Plot the regression line
    plt.plot(years, sea_level, color='red')

    # Filter the data from 2000 onwards
    df_filtered = df[df['Year'] >= 2000]

    # Perform linear regression on the filtered data
    slope, intercept, r_value, p_value, std_err = linregress(df_filtered['Year'], df_filtered['CSIRO Adjusted Sea Level'])

    # Create a range of years from 2000 to the maximum year in the filtered data
    years_extended = range(2000, 2051)

    # Calculate the corresponding sea level values using the regression equation
    sea_level_extended = slope * years_extended + intercept


    # Plot the extended regression line
    plt.plot(years_extended, sea_level_extended, color='blue', label='Extended Regression Line')

    # Set the plot title and axis labels
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()