import pandas as pd 
import numpy as np

# places contents of csv into dataframe 'df' and prints out the percentage of class attended by each student in the class 

pd.read_csv('fake_data.csv', delimiter = ',')

df = pd.read_csv('fake_data.csv', delimiter = ',') 

names = (df.columns)
counter =-1
for x in names: 
    counter = counter +1 
    total = 0 # total is the total length of the class 
    attended = 0 # attended is the amount of time the student actually attends class 
    if counter > 0:
        print(x) # prints out the student's name 
        for i in range(len(df)): 
            total = total+1
            if df.loc[i, x] > 0:
                attended = attended + 1
        print(round((attended/total) * 100))
    





