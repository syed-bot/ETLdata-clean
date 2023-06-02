import pandas as pd

# Load the data from the Excel file
data = pd.read_excel('titanic_data.xls')

# Explore the data
print(data.head())  # Display the first few rows of the DataFrame
print(data.info())  # Get information about the DataFrame
print(data.describe())  # Statistical summary of the data

# Data cleaning
# Handle missing values
data = data.dropna()  # Remove rows with any missing values

# Remove duplicates
data = data.drop_duplicates()

# Data transformation
# Convert data types if needed
data['Age'] = data['Age'].astype(int)  # Convert 'Age' column to integer

# Export the cleaned data to a CSV file
data.to_csv('cleaned_titanic_data.csv', index=False)
