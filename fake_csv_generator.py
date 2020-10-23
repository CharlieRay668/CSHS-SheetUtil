# Import the pandas module, this will be how we handle our data and work with CSV files
import pandas as pd
# Import the datetime module, this is how python can easily work with dates and times
from datetime import date, datetime, time, timedelta
# Import numpy for easy matrix creation
import numpy as np

# REMINDER, this is me creating fake data, this will not be how we actually create data for the attendance machine, 
# this is just to familiarize people with pandas and how the data would be formatted

# Create our hypothetical student names, in reality we will gather these from a class attinorary.
student_names = ['Micheal Jones', 'Charlie Ray', 'Steve House', 'Classic Name', 'Generic Name']

# Start the first time to be at 8:30 in the morning so first period
start_time = time(hour=8, minute=30)
# Add the date onto it
start_time =  datetime.combine(date.today(), start_time)
# Create our times list and add the very fist time
times = [start_time.strftime('%Y/%m/%d-%H:%M')]

# There is 18 5 minute periods in a 90 minute class, we will be adding 5 mins to the time every loop
# Simulates pinging the meet every five minutes
for delta in range(18):
    # Add five minutes to the time
    start_time = start_time + timedelta(minutes=5)
    # Add it to the list but in string form.
    times.append(start_time.strftime('%Y/%m/%d-%H:%M'))

# Create our dataset, your rows (index's) will be the times and your columns will be student names
# np.random.rand creates a matrix of specified size (length(times) = rows, length(student_names = columns)) and populates it with random values
boolean_data = np.random.rand(len(times), len(student_names))
# Because we want our data to be in boolean format (present or absent) instead of random numbers convert the matix to boolean
# There is 100% a better way to do this with pandas but this is a simple way to do it. 
# Anyone who wants to figure out how to do conditional selection with pandas I'll venmo them $1 if they can do this with pandas
for irow, row in enumerate(boolean_data):
    for icol, col in enumerate(row):
        # Make 80% of the data True and 20% false
        if col > 0.8:
            boolean_data[irow][icol] = False
        else:
            boolean_data[irow][icol] = True

# Create our dataframe to be made into a csv, data is our boolean data, index is rows, columns is columns
data = pd.DataFrame(data = boolean_data, index=times, columns=student_names)

# Save our data as a CSV file with name fake_data
data.to_csv('fake_data.csv')

# Show the first little bit of our dataframe so we can see it
print(data.head())