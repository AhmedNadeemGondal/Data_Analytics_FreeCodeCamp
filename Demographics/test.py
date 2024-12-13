import pandas as pd

# Create a DataFrame with sample data
data = {'Column1': [3.14159, 2.71828, 1.61803, 0.57721]}
df = pd.DataFrame(data)

# Calculate the mean and round to the first decimal place
mean_rounded = df['Column1'].mean(round=1)

# Print the rounded mean
print(mean_rounded)
