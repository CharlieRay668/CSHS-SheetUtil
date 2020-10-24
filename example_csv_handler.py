import pandas as pd

# Read in the CSV, make sure to tell it what the index column is, in our case its just the very fist one
attendance_data = pd.read_csv('fake_data.csv', index_col=0)

# Uncomment any part of the code to see what it does

# Prints the beggining part of our data
print(attendance_data.head())

# Print the columns of our data, call .values on it to return a normal python list
# print(attendance_data.columns)

# Print the index's (times) of our data, call .values on it to return a normal python list
# print(attendance_data.index)

# Go through each row in our data, you will be working with pandas row Objects
# for row in attendance_data.iterrows():
#     print(row)

# Go through the row and get the index (time) for that row
# for row in attendance_data.iterrows():
#     print(row[0])

# Go through the row and get the data (Students along with boolean data) for that row
# for row in attendance_data.iterrows():
#     print(row[1])

# Check out a specific student's data for each row
# for row in attendance_data.iterrows():
#     print(row[1]['Charlie Ray'])
